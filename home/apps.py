from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    
    
    def ready(self):
        from django.contrib.auth.models import User
        from .models import CartItem
        def user_cart_count(user):
             return CartItem.objects.filter(cart__is_paid=False, cart__user=user).count()
        User.add_to_class("user_cart_count", user_cart_count)
