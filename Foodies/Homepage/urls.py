from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.Home,name="home"),
    path('About',views.About,name="About"),
    path('uploads',views.uploads,name="upload_images"),
    # path('),include('Homepage.urls')),
    path('Login',views.login_page,name="Login"),
    path('SignUp',views.SignUp,name="SignUp"),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
