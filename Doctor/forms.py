from django.contrib.auth.models import User
from Doctor.models import Profile
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from Patient.models import Patient_appointment,Prescribed_medicine
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

class ProfileForm(forms.ModelForm):
    address = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}

    ) ,max_length=500,required=True)

    speciality = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','row':'1'}

    ) ,max_length=30,required=True)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(label="",choices=GENDER_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    
    DEGREE_CHOICES = (
        ('MB', 'MBBS( Bachelor of Medicine, Bachelor of Surgery)'),
        ('BDS', 'BDS(Bachelor of Dental Surgery)'),
        ('BAMS','BAMS( Bachelor of Ayurvedic Medicine and Surgery)'),
        ('BUMS','BUMS(Bachelor of Unani Medicine and Surgery)'),
        ('BHMS ','BHMS( Bachelor of Homeopathy Medicine and Surgery)'),
        ('MD','MD(Doctor of Medicine)'),
        ('MS','MS(Masters of Surgery)'),
        ('DNB','DNB(Diplomate of National Board )'),
        
    )
    degree = forms.ChoiceField(label="",choices=DEGREE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    EXPERIANCE_CHOICES = (
        ('0', '0 Years'),
        ('1', '1 Years'),
        ('2', '2 Years'),
        ('3', '3 Years'),
        ('4', '4 Years'),
        ('5', '5 Years'),
        ('6', '6 Years'),
    )
    Experience = forms.ChoiceField(label="",choices=EXPERIANCE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    
    DEPARTMENT_CHOICES = (
        ('0', 'Dental'),
        ('1', 'Ophthalmology'),
        ('2', 'Cardiology'),
        ('3', 'For Disabled'),
        ('4', 'Emergency'),
    )
    department = forms.ChoiceField(label="",choices=DEPARTMENT_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    fees = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control'}

    ) ,max_length=30,required=True)
    profile_image = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ('address', 'speciality', 'degree','gender','Experience'
                 ,'fees','department','profile_image')


class passwordchange(PasswordChangeForm):
    old_password = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the old password'}

    ) ,max_length=30, required=True )

    new_password1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the new password'}

    ) ,max_length=30, required=True )

    new_password2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the confirm password'}

    ) ,max_length=30, required=True )

class StatusForm(forms.ModelForm):
    
    class Meta:
        model = Patient_appointment
        fields = ("status",)

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Prescribed_medicine
        fields = ("__all__")
       