from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.Home,name="home"),
    path('About',views.About,name="About"),
    path('uploads',views.uploads,name="upload_images"),
    # path('),include('Homepage.urls')),

]