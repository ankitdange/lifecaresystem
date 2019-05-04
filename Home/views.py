from django.shortcuts import render

def index (request):
    return render(request,'site/index.html')

def aboutus (request):
    return render(request,'site/02-about-us-1.html') 
def service (request):
    return render(request,'site/services-1.html')    
def department (request):
    return render(request,'site/03-department.html')    
def contact (request):
    return render(request,'site/12-contact.html') 
def login (request):
    return render(request,'site/login.html') 
def register (request):
    return render(request,'site/register.html') 
def docreg (request):
    return render(request,'site/logdoctor.html')  
def preg (request):
    return render(request,'site/pregister.html')        
def forgot (request):
    return render(request,'site/forgot.html')
def pforgot (request):
    return render(request,'site/pforgot.html') 
       
