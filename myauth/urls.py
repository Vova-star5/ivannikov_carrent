from django.urls import path
from .views import *


app_name = "myauth"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"), 
    path("profile/", AboutMeView.as_view(), name="profile"), 
    path("profile/<pk>", AboutMeView.as_view(), name="profile"), 
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("orders/", ordersListView.as_view(), name="orders"),
]
