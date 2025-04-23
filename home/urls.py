
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="home-page"),
    path('home/', views.Home, name="home-page"),
    path('logout/',views.Logout,name="logout"),
    path('Login/',views.Login,name="Login"),
    path('Register/',views.Register,name="Register"),
    path("cart/",views.cart,name="cart"),
    path("Add_to_cart/<pizza_uid>",views.Add_to_cart,name="Add_to_cart"),
    path("RemoveItem/<uuid:item_uid>/", views.RemoveItem, name="RemoveItem")
    
    
]
