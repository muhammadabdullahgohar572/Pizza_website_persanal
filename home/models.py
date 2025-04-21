from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True);
    created_at=models.DateTimeField(auto_now_add=True);
    updated_at=models.DateTimeField(auto_now_add=True);
    class Meta:
        abstract=True
        


class PizzaCategory(BaseModel):
    Category_name=models.CharField(default=200);
    

class Pizza(BaseModel):
    Category=models.ForeignKey(PizzaCategory,on_delete=models.CASCADE,related_name="Pizza")
    Pizza=models.CharField(default=100);
    price=models.IntegerField(max_length=200);
    images=CloudinaryField('images')
    


class Cart(BaseModel):
    cart=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="carts")
    is_paid=models.BooleanField(default=False)
    

    

      