from django import forms

class ImageForm(forms.Form):
    
    #image = forms.ImageField(upload_to="photos/images")
    image_name= forms.CharField(max_length=100)
    image_desc =forms.CharField(max_length=1000)
    