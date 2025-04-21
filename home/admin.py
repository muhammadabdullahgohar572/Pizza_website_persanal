from django.contrib import admin
from .models import Pizza,PizzaCategory,Cart,CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display=['cart','is_paid','created_at']
    list_filter = ('is_paid',)
    search_fields = ('user__username',)
    
    
admin.site.register(Pizza)
admin.site.register(PizzaCategory)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
