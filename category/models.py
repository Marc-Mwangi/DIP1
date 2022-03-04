from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = models.CharField(max_length=100)
    category_desc = models.CharField(max_length=1000)

    #Representation in admin dashboard or views
    def __str__(self) -> str:
        return self.category_name