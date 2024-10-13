from django.http import HttpResponse

def Home(request):
    return HttpResponse("Home Page")

def About(request):
    return HttpResponse("Hello About Page")