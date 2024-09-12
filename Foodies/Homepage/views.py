from django.shortcuts import render,redirect
from .models import Foodiee
from .forms import UploadForms
# Create your views here.
from django.http import HttpResponse
# Food = [{"name":"Food1","Desc":"Ready to eat food."},
# {"name":"Food2","Desc":"Ready to eat healthy food2."},{"name":"Food3","Desc":"Ready to eat food3."}]

def Home(request):
    Food=Foodiee.objects.all() #to display all the values in the database
    context={'Food':Food}
    return render(request,"home.html",context)

def About(request):
    return render(request,"about.html")

def uploads(request):
    if request.method == 'POST':
        form = UploadForms(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST) #to check what is happening when form is submitted
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForms()
    return render(request,"uploads.html",{'form':form})