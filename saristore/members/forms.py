from django.forms import ModelForm
from .models import *

#These are the forms that will supply the information to their respective functions in views.py
class UpdateStockForm(ModelForm):
    class Meta:
        model = Product
        fields = ['item_name', 'unit_price', 'received_quantity']

        

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ["quantity", "amount_received", "issued_to"]

class AddNewItemForm(ModelForm):
    class Meta:
        model = Product
        fields= ["item_name","total_quantity","unit_price"]

