from django import forms
from category.models import Category

class ImageForm(forms.Form):
    
    images = forms.FileField()
    image_name= forms.CharField(max_length=100)
    image_desc =forms.CharField(max_length=1000)
    category= forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'palceholder' : 'Category'
    }))