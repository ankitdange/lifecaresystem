from django.db import models
from django.contrib.auth.models import User
from Doctor.models import Profile
from datetime import datetime, timedelta
from Pharmist.models import Drugs
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
class Patient_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField(default='')
    mobile = models.IntegerField(default='0')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        patient_profile=Patient_profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User) 
    
class Patient_appointment(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient_profile = models.ForeignKey(Patient_profile,on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=254)
    # mobile = models.IntegerField()
    disease = models.TextField()
    date = models.DateField(default=timezone.now)
    STATUS_CHOICES = (
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
    )
    status = models.CharField(max_length=25, choices=STATUS_CHOICES,null=True,blank=True,default="Pending")
    def __str__(self):
        return '{}{}{}{}{}{}'.format(self.id,self.patient_profile,"   ","Appointment Date","  ",self.date)

class Prescribed_medicine(models.Model):
    pmedicine=models.ForeignKey(Patient_appointment ,on_delete=models.CASCADE)
    pdrugs=models.ForeignKey(Drugs,on_delete=models.CASCADE)
    MORNING_CHOICES = (
        ('X', 'X'),
        ('Before Meal', 'Before Meal'),
        ('After Meal', 'After Meal'),
        ('Fasting', 'Fasting'),
    )
    morning = models.CharField(max_length=15, choices=MORNING_CHOICES)
    AFTERNOON_CHOICES = (
        ('X', 'X'),
        ('Before Meal', 'Before Meal'),
        ('After Meal', 'After Meal'),
        ('Fasting', 'Fasting'),
    )
    afternoon = models.CharField(max_length=15, choices=AFTERNOON_CHOICES)
    EVENING_CHOICES = (
        ('X', 'X'),
        ('Before Meal', 'Before Meal'),
        ('After Meal', 'After Meal'),
        ('Fasting', 'Fasting'),
    )
    evening= models.CharField(max_length=15, choices=EVENING_CHOICES)
    units = models.IntegerField()

    def __str__(self):
        return '{}{}{}'.format(self.pmedicine.patient_profile.user.first_name," ",self.pdrugs)

class Sale(models.Model):
    drugsname=models.ForeignKey(Prescribed_medicine, on_delete=models.CASCADE)
    sale=models.BooleanField(default=False)

