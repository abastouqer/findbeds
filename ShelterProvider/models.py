from django.db import models
from django.core.validators import RegexValidator
from Individual.models import User,CountryModel,StatsModel

# Create your models here.

SHELTER_CHOICES = (
       ('Adults', 'Adults'),
       ('Female Only', 'Female Only'),
       ('Male Only', 'Male Only'),
       ('Family Friendly', 'Family Friendly'),
     )
pswrd_regex = RegexValidator(regex=r'[A-Za-z0-9@#$%^&+=]{8,}',
                                 message="Password be at least one Uper,one lower letter, one Number and contain on seven total")
class preData(models.Model):
    username = models.CharField(max_length=50,unique=True,blank=False)
    email = models.EmailField()
    shelter_name = models.CharField(max_length=50,help_text="Shelter name",blank=False)
    address = models.CharField(max_length=50,help_text="Address",blank=False)
    password = models.CharField(validators=[pswrd_regex], max_length=100)
    person_contact_name = models.CharField(max_length=50,help_text="Contact name",blank=False)
    total_beds = models.IntegerField(null=True)
    total_allow_reservation = models.IntegerField(null=True)
    max_hold_time = models.TimeField(null=True)
    state = models.ForeignKey(StatsModel,on_delete=models.CASCADE
                              ,null=True,related_name ="state1")
    city = models.CharField(max_length=20)
    country = models.ForeignKey(CountryModel,on_delete=models.CASCADE
                                ,null=True,related_name ="country1")
    zipcode = models.CharField(max_length=5) 
    goip = models.BooleanField(default=True)
    is_shelter = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username 

class postData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    meal_provider = models.CharField(max_length=15, choices=SHELTER_CHOICES)
    breakfast = models.BooleanField()
    Lunch = models.BooleanField()
    Dinner = models.BooleanField()
    Snacks = models.BooleanField()
    Dogs = models.BooleanField()
    Cat = models.BooleanField()
    PowerOutlets = models.BooleanField()
    ComputerAccess = models.BooleanField()
    WIFI = models.BooleanField()
    Shower = models.BooleanField()
    housrs_intake = models.CharField(max_length=2)
    storage_avaliable = models.BooleanField()
    add_picture = models.ImageField(upload_to='images/',blank=True,null=True)
    discription = models.CharField(max_length=100)
    rules = models.CharField(max_length=200)
    geoip = models.BooleanField()