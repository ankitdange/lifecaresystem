
from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.lablogin,name='labtechlogin'),
    path("logout",views.logout,name="lablogout"),
    path('forgot',views.forgot,name='forgot'),
    path('register',views.register,name='doctor_register'),
    path('dashboard',views.dashbord,name='labdashboard'),
    path('dashboard/delete/<int:id>',views.destroy,name='testdelete'),
    path('dashboard/edit/<int:id>',views.edit,name='testedit'),
    path('dashboard/update/<int:id>', views.update ,name="testupdate"),
    path('dashboard/tests',views.ptest,name='ptest'),
    path('dashboard/change_password',views.change_password,name='change_password'),
    path('dashboard/change_profile',views.image_upload,name='image_upload'),
    path('dashboard/labdatabase',views.Lab_database,name='labdatabase'),
    path('dashboard/report',views.report,name='report'),

]
