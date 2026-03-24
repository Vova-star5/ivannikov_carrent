from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from catalog.models import Car, Order
from catalog.forms import AddOrderForm
from django.urls import reverse, reverse_lazy

def catalog_index(request: HttpRequest):
    
    context = {"cars": Car.objects.all()}
    return render(request, "catalog/catalog-index.html", context=context)

def car_info(request: HttpRequest, pk):
    
    # context = {"cars": Car.objects.all()}
    
    context = {"car": Car.objects.get(pk=pk)}
    return render(request, "catalog/catalog-car_info.html", context=context)


def car_order(request: HttpRequest, pk):
    if request.method == "POST":
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order = Order()
            order.car = Car.objects.get(pk=pk)
            order.delivery_address = form.cleaned_data["delivery_address"]
            order.phone = form.cleaned_data["phone"]
            order.babyseat = form.cleaned_data["babyseat"]
            order.user = request.user
            order.save()
            
            

            
            url = reverse("order_info", kwargs={"pk": order.pk})
            # print(f"new url {url}")
            return redirect(url)
        else:
            return render(request, "catalog/catalog-car_order.html", context={"form": form})

    form = AddOrderForm()
    car = Car.objects.get(pk=pk)
    return render(request, "catalog/catalog-car_order.html", context={"form": form, "car": car})


def order_info(request: HttpRequest, pk):
    context = {"order": Order.objects.get(pk=pk)}
    return render(request, "catalog/catalog-order_info.html", context=context)

def car_list(request: HttpRequest):
    
    context = {"cars": Car.objects.all()}
    return render(request, "catalog/catalog_cars.html", context=context)

def about(request: HttpRequest):
    
    context = {"cars": Car.objects.all()}
    return render(request, "catalog/catalog-about.html", context=context)

def contacts(request: HttpRequest):
    return render(request, "catalog/catalog_contacts.html")