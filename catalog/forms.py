from django.forms.models import ModelForm
from catalog.models import Order
from django.core import validators

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "lastname", "name","surname", "phone", "email", "delivery_adress", "babyseat"
        labels = {"lastname": "Фамилия", "name": "Имя", "surname": "Отчество", "delivery_adress": "Адрес", "phone": "Телефон"}
        

        

