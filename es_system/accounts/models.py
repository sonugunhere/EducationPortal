import email
from email.policy import default
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)   
class SchoolManagement(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    school = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=12)
    dise_code = models.IntegerField()
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    school_type = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    confirm_password =models.CharField(max_length=10)

    def __str__(self):
        return self.school
    
GENDER_CHOICES = (
    ('Male', 'Male'),
     ('male', 'male'),
    ('Female', 'Female'),
    ('female', 'female'),
    ('others', 'others'),

) 

class StudentRegisteration(models.Model):
    school=models.ForeignKey(SchoolManagement,on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    email = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length = 12)
    father_name = models.CharField(max_length = 30)
    mother_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    dob = models.DateField(blank=True,null=True)
    standard = models.CharField(max_length=12)
    gender = models.CharField(choices = GENDER_CHOICES,max_length=10,default='Male')
    batch = models.CharField(max_length=10)
    adhar_card=models.CharField(max_length=12)
    
    def __str__(self):
        return self.first_name


    def clean(self):
       
            if not len(self.contact_no) == 10:

                raise ValidationError(
                    {'contact_no': "contact number should have at least 10 digit"})
            

            if not len(self.adhar_card) == 12:
                raise ValidationError(
                    {'adhar_card': "adhar_card number should have at least 12 digit"})
        
  
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


