from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from Individual.models import User
class ShelterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username","first_name","last_name","org_full_name","position","password","email",
                  "phone","address","state","country","zipcode","goip")
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)
    
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