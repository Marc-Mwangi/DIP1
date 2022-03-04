from tkinter import image_names
from django.db import models
from category.models import Category

# Create your models here.

class Image(models.Model):
    
    image_name = models.CharField(max_length=50)
    image_slug =models.CharField(max_length=100)
    image_desc =models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now= True)
    
    category= models.ForeignKey(Category, on_delete= models.CASCADE)
    #Representation of what will be represented in view or admin dashboard
    
    def __str__(self) -> str:
        return self.image_name
