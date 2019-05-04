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
from Pharmist.forms import DrugsForm,Drugsupdate
from Patient.models import Prescribed_medicine,Sale
from django import forms
def Pharmist_login(request):
    if request.method == 'POST':
                username = request.POST.get('username')
                password=request.POST.get('password')
                user=auth.authenticate(username=username,password=password)
                if user:
                        if user.groups.filter(name="Pharmist"):
                                if user.is_active:
                                        auth.login(request,user)
                                        return redirect(reverse('phdashboard'))
                        else:
                                messages.error(request," you are not authorised to access this page")
    
    return render(request,'remark-405/classic/base/html/pages/login.html')
def add_medicine(request):
    if request.method == "POST":
        form=DrugsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("./dashboard/addmedicine")
            messages.success(request,"Medicine Add To The Database")
    else:
        form=DrugsForm()
    context={
        "form":form
            }
    return render(request,'remark-405/classic/base/html/dashboard/addmedicine.html',context)
def prescribed_medicine(request):
    pmed=Prescribed_medicine.objects.all()
    context={
        "p":pmed
    }
    return render(request,'remark-405/classic/base/html/dashboard/pmedicine.html',context)
def forgot(request):
    return render(request,'remark-405/classic/base/html/pages/forgot-password.html')
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('drugsname','sale')  

def salemedicine(request,id):
    sale=Drugs.objects.get(id=id)
    forms=SaleForm()
    context={
        "f":forms,
        "s":sale,
    }
    return render(request,'remark-405/classic/base/html/dashboard/sale.html',context)



def medicine_database(request):
    # fetch all the medicine from Drugs model
    medicines=Drugs.objects.all()
    context={
        "m":medicines
    }
    return render(request,'remark-405/classic/base/html/dashboard/medicinedatabase.html',context)
def update(request, id):  
    medicines = Drugs.objects.get(id=id)  
    form = Drugsupdate(request.POST, instance = medicines)  
    if form.is_valid():  
        form.save()  
        return HttpResponse("update")  
    return render(request, 'remark-405/classic/base/html/dashboard/medicinedatabase.html', {'s': medicines})

def dashbord(request):
    return render(request,'remark-405/classic/base/html/dashboard/v2.html')
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

    return render(request,'remark-405/classic/base/html/dashboard/change-password.html', {
        'form': form
                        })


def image_upload(request):
    return render(request,'remark-405/classic/base/html/dashboard/imageupload.html')
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
        return render(request, 'remark-405/classic/base/html/dashboard/setting.html', {
            'user_form': user_form,
            'profile_form': profile_form
                        })
def bill(request):
    return render(request,'remark-405/classic/base/html/dashboard/bill.html')
def doc_logout(request):
     auth.logout(request)
     return redirect('./login')


