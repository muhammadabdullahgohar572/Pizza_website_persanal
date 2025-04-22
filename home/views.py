from django.shortcuts import render, get_object_or_404, redirect
from .models import Pizza, PizzaCategory, Cart, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
