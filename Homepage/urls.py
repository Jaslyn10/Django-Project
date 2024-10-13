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
    path('Logout',views.logout_user,name="Logout"),
    path('Product/<int:id>',views.product_view,name="Product"),
    path('addWish/<int:id>',views.wish_list,name="addWish"),
    path('addCart/<int:id>',views.cart_list,name="addCart"),
    path('show_cartList',views.show_cartList,name="show_cartList"),
    path('show_wishList',views.show_wishList,name="show_wishList"),
    path('show_wishList/removewish/<int:id>/',views.remove_wish,name='removewish'),
    path('SignUp',views.SignUp,name="SignUp"),
    path('dummy',views.show_api,name="dummy"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
