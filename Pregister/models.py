from django.db import models
class add_Pregister(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    age=models.IntegerField()
    email = models.EmailField(max_length=254)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile=models.IntegerField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField( max_length=50)
    


