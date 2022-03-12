from django.shortcuts import render

from image.forms import ImageForm

# Create your views here.
def images(request):
    
    if request.method == 'POST':
        
        form = ImageForm(request.POST)
        
        if form.is_valid():
            image_name= form.cleaned_data["image_name"]
            image_desc = form.cleaned_data["image_desc"]
            
            print(image_name)
            print(image_desc)
    form = ImageForm()
    
    context ={
        'form': form
    }
    return render(request, 'index.html', context)
