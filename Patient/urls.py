from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
      path('login',views.patient_login,name='patient-loginhere'),
      path('register',views.register,name='patient_register'),
      path('forgot',views.forgot,name='patient_forgot'),
      path('dashboard',views.patient_dashbord,name='patient_dashboard'),
      path('dashboard/appointment',views.patient_appointment,name='patient_appointment'),
      path('logout',views.logout,name='patient_logout'),
      path("dashboard/status",views.appointment_status,name="status"),
      path("dashboard/mymedicine",views.pmedicine,name="mymedicine"),
      path('dashboard/change-password',views.patient_change_password,name='patient_changepassword'),
      path('dashboard/profile',views.patient_profile,name='patient_profile'),
      path('dashboard/setting',views.patient_settings,name='patient_profile'),
      path('dashboard/patient_profile',views.Patient_update_profile,name='patient_user_profile')
]
