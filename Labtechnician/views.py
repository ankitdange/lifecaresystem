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
from Pharmist.forms import DrugsForm
from Labtechnician.forms import AddtestForm
from Labtechnician.models import Add_test,Prescribed_test

from django.shortcuts import render

def lablogin(request):
    if request.method == 'POST':
                username = request.POST.get('username')
                password=request.POST.get('password')
                user=auth.authenticate(username=username,password=password)
                if user:
                        if user.groups.filter(name="Labtechnician"):
                                if user.is_active:
                                        auth.login(request,user)
                                        return redirect(reverse('labdashboard'))
                        else:
                                messages.error(request," you are not authorised to access this page")
    return render(request,'remark-407/classic/base/html/pages/login.html')
def forgot(request):
    return render(request,'remark-403/classic/base/html/pages/forgot-password.html')
def register(request):
    return render(request,'remark-403/classic/base/html/pages/register.html')
def dashbord(request):
    return render(request,'remark-407/classic/base/html/dashboard/v2.html')
def change_password(request):
    return render(request,'remark-403/classic/base/html/dashboard/change-password.html')
def image_upload(request):
    return render(request,'remark-403/classic/base/html/dashboard/imageupload.html')
def Lab_database(request):
        data=Add_test.objects.all()
        context={
                "data":data
        }
        return render(request,'remark-407/classic/base/html/dashboard/labdatabase.html',context)
def report(request):
        if request.method == "POST":
                form=AddtestForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Test Succesfully add to database",fail_silently=True)
                        return redirect("./report")
        else:
                form=AddtestForm()
                
        context={
                "f":form
        }
        return render(request,'remark-407/classic/base/html/dashboard/report.html',context)
def destroy(request, id):
        try:
                tdelete =Add_test.objects.get(id=id)
                tdelete.delete()  
                messages.success(request,f"Test {tdelete} delete")
                return HttpResponse("Iteam Delete")
        except Add_test.DoesNotExist:
                return HttpResponse("iteam not found")
def edit(request, id):
        try:  
                tedit = Add_test.objects.get(id=id)  
                return render(request,'remark-407/classic/base/html/dashboard/edit.html', {'tedit':tedit})
        except Add_test.DoesNotExist:
                return HttpResponse("<h1>Test not found</h1>")

def update(request, id):  
    tedit = Add_test.objects.get(id=id)  
    form = AddtestForm(request.POST, instance = tedit)  
    if form.is_valid():  
        form.save()  
        return HttpResponse("test update")
    return render(request, 'remark-407/classic/base/html/dashboard/edit.html', {'tedit':tedit})
def ptest(request):
        tests=Prescribed_test.objects.all()
        context={
                't':tests
        }
        return render(request,'remark-407/classic/base/html/dashboard/prescribedtest.html',context)
def logout(request):
     auth.logout(request)
     return redirect('./login') 