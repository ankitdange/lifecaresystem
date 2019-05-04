from django.db import models
from django.contrib.auth.models import User
from Patient.models import Patient_appointment,Prescribed_medicine
from Labtechnician.models import Prescribed_test
class Receptionist_profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile_no=models.IntegerField()

    def __str__(self):
        return self.user

class Bill(models.Model):
    appointmentbill=models.ForeignKey(Patient_appointment, on_delete=models.CASCADE)
    medicine=models.ForeignKey(Prescribed_medicine, on_delete=models.CASCADE)
    tests=models.ForeignKey(Prescribed_test, on_delete=models.CASCADE)