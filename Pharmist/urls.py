
from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.Pharmist_login,name='phlogin'),
    path('logout',views.doc_logout,name='logout'),
    path('forgot',views.forgot,name='forgot'),
    path('dashboard/sale/<int:id>',views.salemedicine,name='salemedicine'),
    path('dashboard/update/<int:id>',views.update,name='update'),
    path('dashboard/addmedicine',views.add_medicine,name='addmedicine'),
    path('dashboard/database',views.medicine_database,name='database'),
    path('dashboard/pmedicine',views.prescribed_medicine,name='pmedicine'),
    path('dashboard',views.dashbord,name='phdashboard'),
    path('dashboard/change_password',views.change_password,name='change_password'),
    path('dashboard/change_profile',views.image_upload,name='image_upload'),
    path('dashboard/settings',views.settings,name='settings'),
    path('dashboard/bill',views.bill,name='bill'),
    

]
