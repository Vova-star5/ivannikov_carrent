from django.forms.models import ModelForm
from catalog.models import Order
from django.core import validators

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "phone", "delivery_address", "babyseat"
        labels = {"delivery_address": "Адрес", "phone": "Телефон"}
        

        

