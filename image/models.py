from tkinter import image_names
from django.db import models

# Create your models here.

class Image(models.Model):
    
    image_name = models.CharField(max_length=50)
    image_slug =models.CharField(max_length=100)
    image_desc =models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now= True)
    
    
