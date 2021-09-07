from django.core import validators
from django.forms import ModelForm
from django import forms
from .models import PlaceOrder

class OrderRegistration(forms.ModelForm):
    class Meta:
        model = PlaceOrder
        fields = ['phone','address','city','state','zipcode']
        labels = {
            'phone':'Enter Mobile Number',
            'address':'Address',
            'city':'City',
            'state':'State',
            'zipcode':'Zipcode'
        }
        widgets = {
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter mobile number','autocomplete':'off'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address','autocomplete':'off'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter city','autocomplete':'off'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter state','autocomplete':'off'}),
            'zipcode':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter zipcode','autocomplete':'off'}),
        }
        error_messages = {
            'phone':{'required':'Mobile number has required...!'},
            'address':{'required':'Address has required...!'},
            'city':{'required':'City has required...!'},
            'state':{'required':'State has required...!'},
            'zipcode':{'required':'Zipcode has required...!'},
        }
 