from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ShelterProvider.models import postData,preData
class ShelterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = preData
        fields = ("username","shelter_name","address","password","email",
                  "phone","city","state","country","zipcode","total_beds","total_allow_reservation","max_hold_time","goip")
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return preData.objects.create(**validated_data,is_shelter=True)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        
        instance.username = validated_data.get('username', instance.username)
        instance.shelter_name = validated_data.get('shelter_name', instance.shelter_name)
        instance.address = validated_data.get('address', instance.address)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.person_contact_name = validated_data.get('person_contact_name', instance.person_contact_name)
        
        instance.total_beds= validated_data.get('total_beds', instance.total_beds)
        instance.total_allow_reservation= validated_data.get('total_allow_reservation', instance.total_allow_reservation)
        instance.max_hold_time= validated_data.get('max_hold_time', instance.max_hold_time)
        
        instance.goip= validated_data.get('goip', instance.goip)
        instance.save()
        return instance
    

class ShelterEditUserSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = postData
        fields = ("user","meal_provider","breakfast","Lunch","Dinner",
                  "Snacks","Dogs","Cat","PowerOutlets","ComputerAccess","WIFI","Shower","storage_avaliable","add_picture","discription","rules","housrs_intake","goip")
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return postData.objects.create(**validated_data,is_shelter=True)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        
        instance.user = validated_data.get('user', instance.user)
        instance.meal_provider = validated_data.get('meal_provider', instance.meal_provider)
        instance.breakfast = validated_data.get('breakfast', instance.address)
        instance.Lunch = validated_data.get('Lunch', instance.Lunch)
        instance.Dinner = validated_data.get('Dinner', instance.Dinner)
        instance.Snacks = validated_data.get('Snacks', instance.Snacks)
        instance.Dogs = validated_data.get('Dogs', instance.Dogs)
        instance.Cat = validated_data.get('Cat', instance.Cat)
        instance.PowerOutlets = validated_data.get('PowerOutlets', instance.PowerOutlets)
        instance.ComputerAccess = validated_data.get('ComputerAccess', instance.ComputerAccess)
        instance.WIFI = validated_data.get('WIFI', instance.WIFI)
        
        instance.Shower= validated_data.get('Shower', instance.Shower)
        instance.housrs_intake= validated_data.get('housrs_intake', instance.housrs_intake)
        instance.storage_avaliable= validated_data.get('storage_avaliable', instance.storage_avaliable)
        instance.add_picture= validated_data.get('add_picture', instance.add_picture)
        instance.discription= validated_data.get('discription', instance.discription)
        instance.rules= validated_data.get('rules', instance.rules)
        
        instance.goip= validated_data.get('goip', instance.goip)
        instance.save()
        return instance
    
class ShelterUserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = preData
        fields = ("shelter_name","address",
                  "phone","city""total_beds","total_allow_reservation")