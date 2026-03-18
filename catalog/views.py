from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from catalog.models import Car



def catalog_index(request: HttpRequest):
    
    context = {"cars": Car.objects.all()}
    return render(request, "catalog/catalog-index.html", context=context)

def car_info(request: HttpRequest, pk):
    
    # context = {"cars": Car.objects.all()}
    
    context = {"car": Car.objects.get(pk=pk)}
    return render(request, "catalog/catalog-car_info.html", context=context)