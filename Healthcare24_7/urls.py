"""Healthcare24_7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy as _
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Home.urls")),
    path('Doctor/',include("Doctor.urls")),
    path('Patient/',include("Patient.urls")),
    path('Pharmist/',include("Pharmist.urls")),
    path('Labtechnician/',include("Labtechnician.urls")),
    path('Receptionist/',include("Receptionist.urls")),
    path("dashboard/",include("avatar.urls")),
    path('notifications/', include('notify.urls', 'notifications')),

]
admin.site.site_header = _("LifeCare 24X7 Adminstrations")
admin.site.site_title = "LifeCare 24X7"
admin.site.index_title = "Welcome to Lifecare 24X7 admin area"

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)