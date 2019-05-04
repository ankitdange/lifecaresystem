
from django.urls import path,include
from Doctor import views
urlpatterns = [
    path('login',views.doctor_login,name='doclogin'),
    path('forgot',views.forgot,name='forgot'),
    path('register',views.register,name='doctor_register'),
    path('dashboard/',views.dashbord,name='docdashboard'),
    path('dashboard/change_password',views.change_password,name='change_password'),
    path('dashboard/change_profile',views.image_upload,name='image_upload'),
    path('dashboard/appointments',views.appointment,name='appointment'),
   #path('dashboard/appointments/<int:id>',views.update,name='update'),
   path('dashboard/status/<int:id>',views.appointment_status,name="appstatus"),
    path('dashboard/settings',views.settings,name='docsettings'),
    path('dashboard/medicine/<int:id>',views.medicine,name='medicine'),
    path('dashboard/prescribe',views.prescribe,name='prescribe'),
    path("logout",views.doc_logout,name="doclogout"),
    path("dashboard/patient_report",views.patient_report,name="patient-report"),
    path("dashboard/make_patient_report",views.make_patient_report,name="make_patient-report"),

    path(r'^avatar/', include('avatar.urls'))

   

]
