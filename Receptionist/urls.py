
from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.Receptionist_login,name='login'),
    path("logout",views.logout,name="rlogout"),
    path('forgot',views.forgot,name='forgot'),
    path('register',views.register,name='doctor_register'),
    path('dashboard',views.dashbord,name='Recdashboard'),
    path('dashboard/change_password',views.change_password,name='change_password'),
    path('dashboard/change_profile',views.image_upload,name='image_upload'),
    path('dashboard/settings',views.settings,name='settings'),
    path('dashboard/bill-generate',views.bill_generate,name='bill_generate'),

]
