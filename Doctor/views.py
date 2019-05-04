from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from Doctor.forms import UserForm,ProfileForm,passwordchange,StatusForm,MedicineForm
from Doctor.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from Patient.models import Patient_appointment,Prescribed_medicine
from Pharmist.models import Drugs
from django.forms import ModelForm
from django import forms
def doctor_login(request):
        if request.method == 'POST':

                username = request.POST.get('username')
                password=request.POST.get('password')
                user=auth.authenticate(username=username,password=password)
                if user:
                        if user.groups.filter(name="Doctor"):
                                if user.is_active:
                                        auth.login(request,user)
                                        return redirect(reverse('docdashboard'))
                        else:
                                messages.error(request," you are not authorised to access this page")
       
        return render(request,'remark-403/classic/base/html/pages/login.html')
def forgot(request):
    return render(request,'remark-403/classic/base/html/pages/forgot-password.html')
def register(request):
    return render(request,'remark-403/classic/base/html/pages/register.html')
@login_required(login_url='/Doctor/login')
def dashbord(request):
        print(request.session.session_key)
        return render(request,'remark-403/classic/base/html/dashboard/v2.html')
def change_password(request):
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
        return render(request, 'remark-403/classic/base/html/dashboard/change-password.html', {
        'form': form
                        })

        
    #return render(request,'remark-403/classic/base/html/dashboard/change-password.html')
def image_upload(request):
        return render(request,'remark-403/classic/base/html/dashboard/imageupload.html')

def appointment(request):
        appointment= Patient_appointment.objects.all()
        context={
                "a":appointment,
                
        }
        return render(request,'remark-403/classic/base/html/dashboard/appointment.html',context,)
def appointment_status(request,id):
        form2=Patient_appointment.objects.get(id=id)
        form=StatusForm(request.POST,instance=form2)
        print("ankit=",form2)
        if form.is_valid():
                form.save()
        else:
                form=StatusForm()
        context={
                "form":form,
                "form2":form2
        }
        return render(request,'remark-403/classic/base/html/dashboard/status.html',context)
def settings(request):
        if request.method == 'POST':
                user_form = UserForm(request.POST, instance=request.user)
                profile_form = ProfileForm(request.POST,instance=request.user.profile)
                if user_form.is_valid() and profile_form.is_valid():
                        user_form.save()
                        profile_form.save()
                        messages.success(request, _('Your profile was successfully updated!'))
                        return redirect('./settings')
                else:
                        messages.error(request, _('Please correct the error below.'))
        else:
                user_form = UserForm(instance=request.user)
                profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'remark-403/classic/base/html/dashboard/setting.html', {
                'user_form': user_form,
                'profile_form': profile_form
                        })
        #return render(request, 'remark-403/classic/base/html/dashboard/setting.html')
        #return render(request,'remark-403/classic/base/html/dashboard/setting.html')
def medicine(request ,id):
        appointment= Patient_appointment.objects.get(id=id)
        if request.method == "POST":
                form = MedicineForm(request.POST)
                if form.is_valid():
                        form.save()
                        print("data save hua....!!!!!!!")
        else:
                form = MedicineForm()
                print("data save nahi hua!!!!!!!!")
        context={
                "a":appointment,
                "form":form,
                
        }
        return render(request,'remark-403/classic/base/html/dashboard/medicine.html',context)
def prescribe(request):
    return render(request,'remark-403/classic/base/html/dashboard/prescribe.html')

def patient_report(request):
    return render(request,'remark-403/classic/base/html/dashboard/lab-report.html')

def make_patient_report(request):
    return render(request,'remark-403/classic/base/html/dashboard/make-patient-report.html')


def doc_logout(request):
     auth.logout(request)
     return redirect('./login')