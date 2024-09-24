from django.shortcuts import render,redirect
from .models import Foodiee,FoodImages
from .forms import UploadForms
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
# Food = [{"name":"Food1","Desc":"Ready to eat food."},
# {"name":"Food2","Desc":"Ready to eat healthy food2."},{"name":"Food3","Desc":"Ready to eat food3."}]

def Home(request):
    Food=FoodImages.objects.all() #to display all the values in the database
    context={'Food':Food}
    return render(request,"home.html",context)

def About(request):
    return render(request,"about.html")

@login_required
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

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        print("Is form valid",form)
        if form.is_valid():
            #username #password
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=user_name,password=password)
            if user is not None:
                return redirect('home')
            else:
                return render(request,'login.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    
def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Login')
    else:
        form = UserCreationForm()
        return render(request,'SignUp.html',{'form':form})