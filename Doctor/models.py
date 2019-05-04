from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField(max_length=500)
    speciality = models.CharField(max_length=50)
   
    DEGREE_CHOICES = (
        ('MBBS( Bachelor of Medicine, Bachelor of Surgery)', 'MBBS( Bachelor of Medicine, Bachelor of Surgery)'),
        ('BDS', 'BDS(Bachelor of Dental Surgery)'),
        ('BAMS','BAMS( Bachelor of Ayurvedic Medicine and Surgery)'),
        ('BUMS','BUMS(Bachelor of Unani Medicine and Surgery)'),
        ('BHMS ','BHMS( Bachelor of Homeopathy Medicine and Surgery)'),
        ('MD','MD(Doctor of Medicine)'),
        ('MS','MS(Masters of Surgery)'),
        ('DNB','DNB(Diplomate of National Board )'),
        
    )
    degree = models.CharField(max_length=8, choices=DEGREE_CHOICES)
    
    
    
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #password = models.CharField(max_length=50)
    #confirm_password = models.CharField( max_length=50)
    EXPERIANCE_CHOICES = (
        ('0', '0 Years'),
        ('1', '1 Years'),
        ('2', '2 Years'),
        ('3', '3 Years'),
        ('4', '4 Years'),
        ('5', '5 Years'),
        ('6', '6 Years'),
    )
    Experience = models.CharField(max_length=7, choices=EXPERIANCE_CHOICES)

    DEPARTMENT_CHOICES = (
        ('Dental', 'Dental'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Cardiology', 'Cardiology'),
        ('For Disabled', 'For Disabled'),
        ('Emergency', 'Emergency'),
    )
    department = models.CharField(max_length=45, choices=DEPARTMENT_CHOICES)
    
    fees = models.IntegerField(null=True)
    
    def __str__(self):
        return '{}{}{}{}{}'.format(self.user.username," ",self.department," ","Department")

#     def __str__(self):
#         return self.user.username or self.department

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
    
# class Doctor_profile(models.Model):
#     profile = models.ImageField(upload_to="pictures/%Y/%m/%d" ,null=True,blank=True


