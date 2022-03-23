from math import fabs
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import datetime
import django

now = datetime.now()
GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    
class EthenicityModel(models.Model):
    ethenicity = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ethenicity
    
    
    
class CountryModel(models.Model):
    countries = models.CharField(max_length=50)
    
    def __str__(self):
        return self.countries 

class StatsModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    states = models.CharField(max_length=50)
    
    def __str__(self):
        return self.states

pswrd_regex = RegexValidator(regex=r'[A-Za-z0-9@#$%^&+=]{8,}',
                                 message="Password be at least one Uper,one lower letter, one Number and contain on seven total")
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50,unique=True,blank=False)
    nick_name = models.CharField(max_length=50,help_text="Nick name",blank=False)
    first_name = models.CharField(max_length=50,help_text="First name",blank=False)
    last_name = models.CharField(max_length=50,help_text="Last name",blank=False)
    ethenicity = models.ForeignKey(EthenicityModel,on_delete=models.CASCADE
                                   ,null=True,related_name ="ethenicity1")
    org_full_name = models.CharField(max_length=50,help_text="Org full name",blank=False)
    position = models.CharField(max_length=50,help_text="Position",blank=False)
    address = models.CharField(max_length=50,help_text="Address",blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17,blank=False)
    
    password = models.CharField(validators=[pswrd_regex], max_length=100)
    dob = models.DateField('%Y-%m-%d',null=True)
    state = models.ForeignKey(StatsModel,on_delete=models.CASCADE
                              ,null=True,related_name ="state")
    city = models.CharField(max_length=20)
    country = models.ForeignKey(CountryModel,on_delete=models.CASCADE
                                ,null=True,related_name ="country")
    zipcode = models.CharField(max_length=5) 
    goip = models.BooleanField(default=True)
    
    
    
    create_account = models.DateTimeField(default=django.utils.timezone.now)
    is_individual = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username 