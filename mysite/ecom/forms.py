from django import forms
from ecom.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"