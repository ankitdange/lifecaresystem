from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from Doctor.forms import UserForm,ProfileForm,passwordchange
from Doctor.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from Pharmist.models import Drugs
from Receptionist.models import Bill
from Patient.models import Patient_appointment,Prescribed_medicine
from Labtechnician.models import Prescribed_test
def Receptionist_login(request):
    if request.method == 'POST':
                username = request.POST.get('username')
                password=request.POST.get('password')
                user=auth.authenticate(username=username,password=password)
                if user:
                        if user.groups.filter(name="Receptionist"):
                                if user.is_active:
                                        auth.login(request,user)
                                        return redirect(reverse('Recdashboard'))
                        else:
                                messages.error(request," you are not authorised to access this page")
    return render(request,'remark-406/classic/base/html/pages/login.html')
def forgot(request):
    return render(request,'remark-406/classic/base/html/pages/forgot-password.html')
def register(request):
    return render(request,'remark-406/classic/base/html/pages/register.html')
@login_required(login_url='/Receptionist/login')
def dashbord(request):
    return render(request,'remark-406/classic/base/html/dashboard/v2.html')
@login_required(login_url='/Receptionist/login')
def change_password(request):
    return render(request,'remark-406/classic/base/html/dashboard/change-password.html')
@login_required(login_url='/Receptionist/login')
def image_upload(request):
    return render(request,'remark-406/classic/base/html/dashboard/imageupload.html')
@login_required(login_url='/Receptionist/login')
def settings(request):
    return render(request,'remark-406/classic/base/html/dashboard/setting.html')
@login_required(login_url='/Receptionist/login')
def bill_generate(request):
        bill=Prescribed_medicine.objects.all()
        bill2=Prescribed_test.objects.all()
        
        context={
                "b":bill,
                "b2":bill2
        }
        return render(request,'remark-406/classic/base/html/dashboard/bill.html',context)
def logout(request):
     auth.logout(request)
     return redirect('./login')