from users.models import Profile, CusOrders
from django.contrib.auth.models import User
from django import forms


class ProfformEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'location', 'image', 'user_type']
        
class ProfformCreate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'location', 'image', 'user_type']
        

class UpdateOrder(forms.ModelForm):
    class Meta:
        model = CusOrders
        fields = ['quantity']