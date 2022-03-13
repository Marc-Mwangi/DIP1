from django.contrib import admin
from .models import Image
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'image_slug' :('image_name',)}
    list_display = ("image_name", "image_slug")

admin.site.register(Image, ImageAdmin)
