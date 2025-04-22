
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="home-page"),
    path('home/', views.Home, name="home-page"),
    path('logout/',views.Logout,name="logout"),
    path('Login/',views.Login,name="Login"),
    path('Register/',views.Register,name="Register"),
    
    
    
]
