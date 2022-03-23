from django.shortcuts import render
from category.models import Category
from .models import Image
from image.forms import ImageForm

# Create your views here.
def images(request):
    
    if request.method == "POST" :
        
        images = request.FILES.get("images")
        image_name = request.POST.get("image_name")
        image_desc = request.POST.get("image_desc")
        category = request.POST.get("category")
        
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context={
                    "form": form,
                }
            return render(request, 'index.html', context)
        #Get category associations
        image_category= Category.objects.get(id=category)
        
        image0= Image(images=images, image_name=image_name, image_desc=image_desc, category= image_category)
        
        image0.save()
        
    form = ImageForm()
    
    context ={
        'form': form
    }
    return render(request, 'index.html', context)
