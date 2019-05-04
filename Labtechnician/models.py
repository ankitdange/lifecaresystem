from django.db import models
from Patient.models import Patient_appointment
class add_Labtechnician(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # address = models.TextField()
    # email = models.EmailField(max_length=254)
    degree_choice=(
        ('1','BMLT'),
        ('2','DMLT'),
        ('3','CMLT' ),
        ('4','Bsc(MLT)' ),
        
        )
    degree = models.CharField(max_length=4, choices=degree_choice)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __str__(self):
        return self.first_name

class Add_test(models.Model):
    test_type = models.CharField(max_length=50 )
    fees = models.IntegerField()
    def __str__(self):
        return self.test_type

class Make_labreport(models.Model):
    patient_appointment=models.ForeignKey(Patient_appointment, on_delete=models.CASCADE)
    test_type=models.ForeignKey(Add_test,on_delete=models.CASCADE)
    test_result = models.CharField(max_length=50)
    
class Prescribed_test(models.Model):
    ptest=models.ForeignKey(Patient_appointment, on_delete=models.CASCADE)
    test=models.ForeignKey(Add_test, on_delete=models.CASCADE)
    