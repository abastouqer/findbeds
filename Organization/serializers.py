from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from Individual.models import User
class OrgUserSerializer(serializers.ModelSerializer):

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
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.org_full_name = validated_data.get('org_full_name', instance.org_full_name)
        instance.position = validated_data.get('position', instance.position)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        instance.address = validated_data.get('address', instance.address)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.goip= validated_data.get('goip', instance.goip)
        instance.save()
        return instance