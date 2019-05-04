from django.urls import path
from django.contrib import admin
from Home import views
urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('about_us',views.aboutus,name='aboutus'),
    path('our_services',views.service,name='service'),
    path('our_department',views.department,name='department'),
    path('contact_us',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('Doctor_login',views.docreg,name='doctorreg'),
    path('Doctor_forgot',views.forgot,name='dforgot'),
    path('patients_forget',views.pforgot,name="pforgot"),
    path('patients_register',views.preg,name="preg"),

    ]
