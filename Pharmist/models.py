from django.db import models
from Doctor.models import Profile
class add_Pharmist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField(max_length=254)
    degree_choice=(
        ('1','D.pharma'),
        ('2','B.pharma'),
        ('3','M.pharma' ),
        ('4','B.Ayurvedic' ),
        
        )
    degree = models.CharField(max_length=4, choices=degree_choice)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.first_name

class Drugs(models.Model):
    Brand_Name = models.CharField(max_length=50)
    Unit = models.IntegerField()
    Active_ingredients = models.CharField(max_length=50)
    #strength = models.CharField(max_length=50,null=True)
    price = models.IntegerField()
    def __str__(self):
        return self.Brand_Name

