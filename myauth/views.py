from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from .models import Profile
from catalog.models import Order




class LoginView(LoginView):
    template_name = "myauth/login.html"
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy("myauth:profile")
        
    


class MyLogoutView(LogoutView):
     
    #  next_page = reverse_lazy("index")
     def get_success_url(self):
        return reverse_lazy("index")


class AboutMeView(UpdateView):
     model = Profile
     template_name = "myauth/about-me.html"
     success_url = reverse_lazy("myauth:login")
     fields = "name", "lastname"
     pk_url_kwarg = 1
     def get_object(self):
        return self.request.user.profile
        
     
     


     def get_success_url(self) -> str:
        return reverse("myauth:profile", kwargs={"pk": self.object.pk})


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/registration.html"
    success_url = reverse_lazy("myauth:login")

    def form_valid(self, form: UserCreationForm) -> HttpResponse:
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        
        return response
    

class ordersListView(ListView):
    #  model = Order
     template_name = "myauth/orders_list.html"
     context_object_name = "orders"
    #  queryset = Order.objects.filter(user = requ)
     def get_queryset(self):
         
         return  Order.objects.filter(pk=self.request.user.pk)
    