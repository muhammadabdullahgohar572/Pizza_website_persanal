from django.shortcuts import render,get_object_or_404
from .models import Pizza,PizzaCategory,Cart,CartItem
# Create your views here.
def Home(request):
    pizza = Pizza.objects.all()
    return render(request, "Home.html", {'pizzas': pizza})
