"""Creating Pet Form"""
from django import forms
from django.forms import ModelForm
from .models import Pet

#create form here

class PetForm(ModelForm):
    """PETFORM"""
    class Meta:
        """Linking with models"""
        model = Pet
        fields = ('name','breed','age','description','image')
        labels = {
                'name':'',
                'breed':'',
                'age':'',
                'description':'',
                'image':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'breed':forms.TextInput(attrs={'class':'form-control','placeholder':'Breed'}),
            'description':forms.TextInput(attrs=
            {'class':'form-control','placeholder':'Description'}),
        }
