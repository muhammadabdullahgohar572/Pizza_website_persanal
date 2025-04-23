from django.shortcuts import render, get_object_or_404, redirect
from .models import Pizza, PizzaCategory, Cart, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def Home(request):
    pizza = Pizza.objects.all()
    return render(request, "Home.html", {"pizzas": pizza})


def Register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name");
        last_name=request.POST.get("last_name");
        username=request.POST.get("username");
        email=request.POST.get("email");
        password1=request.POST.get("password1");
        password2=request.POST.get("password2");
        
        if password1 !=password2 :
            messages.error(request,"Passwords do not match")
            return redirect("Register")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"User name is  Already Exit")
            return redirect("Register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email is Already Exit")
            return redirect("Register")
        
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password1,
            
        )
        messages.success(request,"User Account succussfully")
        return redirect("Login")
        
        
    return render(request, "register.html")


def Login(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is  not None:
                login(request, user)
                messages.success(request, f"Login Successfully {user.username}")
                return redirect("home-page")          
            else:
                messages.error(request, "User Or Password")
                return redirect("Login")
        except Exception as e:
            messages.error("This is  a error exception {str(e)}")
            return redirect("home-page")
    return render(request, "Login.html")



def Logout(request):
    logout(request)
    return redirect("home-page")


def cart(request):
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
        return render(request, "cart.html", {"cart": cart})
    except Cart.DoesNotExist:
        return render(request, "cart.html", {"cart": None})
    
 
    
    
def Add_to_cart(request,pizza_uid):
    user=request.user;
    pizza_obj=Pizza.objects.get(uid=pizza_uid)
    cart,_=Cart.objects.get_or_create(user=user,is_paid=False)
    cart=CartItem.objects.create(
      Pizza=pizza_obj,
      cart=cart
    )   
    return redirect ("/home")    
    
    
    
    
    
def RemoveItem(request, item_uid):
    try:
        cart_item = get_object_or_404(CartItem, uid=item_uid, cart__user=request.user)
        cart_item.delete()
        messages.success(request, "Item removed from cart")   
        return redirect('cart')
    except Exception as e:
        messages.error(request, "Error removing item from cart")
        return redirect('cart')