from django import forms
from .models import house

class form_names(forms.ModelForm):
    class Meta :     
        model = house
        fields = '__all__'
    
 