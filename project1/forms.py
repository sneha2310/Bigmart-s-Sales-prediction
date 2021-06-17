from django.forms import ModelForm, widgets , TextInput
from django import forms
from .models import User
class Register(ModelForm):
        class Meta:
                model = User
                fields = ['Item_Identifier', 'Item_Weight', 'Item_Fat_Content', 'Item_Type', 'Item_MRP', 'Outlet_Identifier', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']
                widgets = {
                        'Item_Identifier' : forms.TextInput(attrs={'class':'form-control'}),
                        'Item_Weight': forms.TextInput(attrs={'type':'number'}),
                        'Item_Fat_Content': forms.TextInput(attrs={'class':'form-control'}),
                        'Item_Type' : forms.TextInput(attrs={'class':'form-control'}),
                        'Item_MRP': forms.TextInput(attrs={'type':'number'}),
                        'Outlet_Identifier': forms.TextInput(attrs={'class':'form-control'}),
                        'Outlet_Size': forms.TextInput(attrs={'class':'form-control'}),
                        'Outlet_Location_Type': forms.TextInput(attrs={'class':'form-control'}),
                        'Outlet_Type': forms.TextInput(attrs={'class':'form-control'})

                }