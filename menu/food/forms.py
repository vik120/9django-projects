from django.forms import forms, ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_price', 'item_desc', 'item_image']
