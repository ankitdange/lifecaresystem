from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Patient.models import Patient_appointment,Prescribed_medicine
from django.db.models import QuerySet
from Doctor.models import Profile
from Patient.models import Patient_profile
from django.contrib.auth.forms import PasswordChangeForm
class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the username'}

    ) ,max_length=30, required=True )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the firstname'}

    ) ,max_length=30, required=True )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the lastname'}

    ) ,max_length=30, required=True )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the email'}

    ) ,max_length=30, required=True )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the password'}

    ) ,max_length=30, required=True )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the confirm password'}

    ) ,max_length=30, required=True )
    
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
   

class Appointment(forms.ModelForm):
    date = forms.DateField(label="Date",widget=forms.TextInput(attrs={'class':'form-control','type':'date'}

    ) ,required=True)
    disease = forms.CharField(label="Disease",widget=forms.Textarea(attrs={'class':'form-control','rows':4, 'cols':15}

    ) ,required=True)
    
    
    class Meta:
        model=Patient_appointment
        fields =("profile","disease","date","patient_profile")

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control'}

    ) ,max_length=30,required=True)
    
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control'}

    ) ,max_length=30,required=True)

    email = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','row':'1'}

    ) ,max_length=30,required=True)

    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class passwordchange(PasswordChangeForm):
    old_password = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the old password'}

    ) ,max_length=30, required=True )

    new_password1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the new password'}

    ) ,max_length=30, required=True )

    new_password2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the confirm password'}

    ) ,max_length=30, required=True )




class Patient_profileForm(forms.ModelForm):
    
    
    class Meta:
        model = Patient_profile
        fields = ("gender","address","mobile",)

class Update_patient_profileForm(forms.ModelForm):
    user="request.user.username"
    class Meta:
        model = Patient_profile
        fields = ("address","gender","mobile","user")




