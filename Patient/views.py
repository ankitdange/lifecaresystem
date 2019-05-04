from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,Appointment
from django import forms
from Patient.models import Patient_appointment,Patient_profile,Prescribed_medicine
from Doctor.models import Profile
from django.urls import reverse
from Patient.forms import UserForm,Patient_profileForm,passwordchange,Update_patient_profileForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from notify.signals import notify
def patient_login(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password=request.POST.get('password')
          user=auth.authenticate(username=username,password=password)
          if user:
               if user.is_active:
                    auth.login(request,user)
                    return redirect(reverse('patient_dashboard'))
                    
          else:
               messages.error(request,"username and password did not match.")

       
     return render(request,'remark-404/classic/base/html/pages/login-v2.html')
def forgot(request):
    return render(request,'remark-404/classic/base/html/pages/registration/password_reset_form.html')
def register(request):
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               raw_password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=raw_password)
               login(request, user)
               return redirect('./dashboard')
     else:
        form = SignUpForm()
     return render(request,'remark-404/classic/base/html/pages/register-v2.html', {'form': form})

@login_required(login_url='/Patient/login') #redirect when user is not logged in
def patient_dashbord(request):
     if request.user.groups.all != "Doctor" and request.user.is_superuser == False:
          return render(request,'remark-404/classic/base/html/dashboard/v2.html')
     else:
          a=request.user.username
          messages.error(request,f"You're authenticated as {a}")
          messages.error(request,"but you're not authorized to access this page")
          auth.logout(request)
          return redirect('./login')
    


def patient_appointment(request):
     c=Patient_profile.objects.all()
     doc=Profile.objects.all()
     xr=Profile.objects.get(id=1)
     if request.method == "POST":
          profile=request.POST['profile']
          form=Appointment(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,"Appointment Has Been Placed !")
               print("data save hua !")
     else:
          form=Appointment()
          print("data save nahi hua !")
     context=  {
          "f":form,
          'c':c,
          'doc':doc,
          "x":xr
               }
     return render(request ,'remark-404/classic/base/html/dashboard/appointment.html',context)

def patient_change_password(request):
     if request.method == 'POST':
                form = passwordchange(request.user, request.POST)
                if form.is_valid():
                        user = form.save()
                        update_session_auth_hash(request, user)  # Important!
                        messages.success(request, 'Your password was successfully updated!')
                        return redirect('/change_password')
                else:
                        
                        messages.error(request, 'Please enter the correct password.')
     else:
          form = passwordchange(request.user)
     return render(request ,'remark-404/classic/base/html/dashboard/change-password.html',{"form":form})
def patient_settings(request):
     try:
          if request.method == 'POST':
               user_form = UserForm(request.POST, instance=request.user)
               profile_form = Patient_profileForm(request.POST,instance=request.user.patient_profile)
               if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()
                    messages.success(request, _('Your profile was successfully updated!'))
                    return redirect('./setting')
               else:
                    messages.error(request, _('Please correct the error below.'))
          else:
               user_form = UserForm(instance=request.user)
               profile_form = Patient_profileForm(instance=request.user.patient_profile)
     
          context={
          "form":user_form,
          "form2":profile_form
                    }
          return render(request,'remark-404/classic/base/html/dashboard/setting.html',context)
     except ObjectDoesNotExist:
          return HttpResponse("<div class='container'><h3>Data Not Found Please Update The Patient Profile</h3> </div>")
          print("datanotfound")
def Patient_update_profile(request):
     data=Patient_profile.objects.all()
     if request.method == 'POST':
          form=Update_patient_profileForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect("./dashboard/patient_profile")
               print("data save hua")
     else:
          form=Update_patient_profileForm()
     context={
          "form":form,
          "d":data
          }
     return render(request,'remark-404/classic/base/html/dashboard/patient_profile.html',context)        
def logout(request):
     auth.logout(request)
     return redirect('./login')
def patient_profile(request):
     return render(request,'remark-404/classic/base/html/dashboard/profile.html')

def appointment_status(request):
     c=Patient_appointment.objects.filter(patient_profile=request.user.patient_profile.id)
     context={
          "c":c
     }
     return render(request,'remark-404/classic/base/html/dashboard/appointmentstatus.html',context)

def pmedicine(request):
     pmed=Prescribed_medicine.objects.all()
     context={
          "p":pmed
     }
     return render(request,'remark-404/classic/base/html/dashboard\prescribe.html',context)