from django.db import models

from Individual.models import User

# Create your models here.

SHELTER_CHOICES = (
       ('Adults', 'Adults'),
       ('Female Only', 'Female Only'),
       ('Male Only', 'Male Only'),
       ('Family Friendly', 'Family Friendly'),
     )
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