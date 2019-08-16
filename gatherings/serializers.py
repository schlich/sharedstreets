from gatherings import models
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class PersonSerializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=20, source='first_name')
    LastName = serializers.CharField(max_length=30, required=False, source='last_name')
    Pronoun = serializers.CharField(max_length=20, required=False, source='pronouns')
    Phone = serializers.CharField(max_length=20, required=False, source='phone')
    Email = serializers.EmailField(required=False, source='email')
    Birthday = serializers.DateField(required=False, source='birthday')
    LeadershipInterested = serializers.BooleanField(required=False, source='leadership_interested')
    LeadershipTrained = serializers.BooleanField(required=False, source='leadership_trained')
    Connection = serializers.CharField(max_length=40, source='connection')
    Participation = serializers.CharField(max_length=40, source='participation')

    def create(self, validated_data):
        return models.Person.objects.create(**validated_data)
