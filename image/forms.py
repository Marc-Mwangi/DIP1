from tkinter import image_names
from django import forms

class ImageForm(forms.form):
    
    image = forms.ImageField(upload_to="photos/images")
    image_name= forms.forms.CharField(max_length=100)
    image_desc =forms.forms.CharField(max_length=1000)
    