from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from Individual.models import User
class IndividualUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username","first_name","ethenicity","gender","password","dob",
                  "phone","state","country","goip")
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data,is_individual = True)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        
        instance.first_name = validated_data.get('nick_name', instance.first_name)
        instance.username = validated_data.get('username', instance.username)
        instance.ethenicitye = validated_data.get('ethenicitye', instance.ethenicitye)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.goip= validated_data.get('goip', instance.goip)
        instance.save()
        return instance