from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PizzaCategory(BaseModel):
    Category_name = models.CharField(max_length=200)

    def __str__(self):
        return f"Pizza Category {self.Category_name}"


class Pizza(BaseModel):
    Category = models.ForeignKey(
        PizzaCategory, on_delete=models.CASCADE, related_name="Pizza"
    )
    SIZE_CHOICES = [
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    ]
    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        default='medium'
    )
    Pizza = models.CharField(max_length=100)
    price = models.IntegerField(max_length=200)
    images = CloudinaryField("images")


class Cart(BaseModel):
    cart = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="carts"
    )
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pizza Category {self.cart}"


class CartItem(BaseModel):
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")

    def __str__(self):
        return f"{self.cart}, {self.Pizza}"
