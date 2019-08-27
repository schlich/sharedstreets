from gatherings import models
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class PersonSerializer(serializers.Serializer):
    airtableID = serializers.CharField(max_length=50)
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


class GatheringSerializer(serializers.Serializer):
    airtableID = serializers.CharField(max_length=20)
    ClassName = serializers.CharField(max_length=50, source='name')
    ClassAuthor = serializers.SlugRelatedField(many=True, slug_field='airtableID',
                                               queryset=models.Person.objects.all(), source='authors')
    Summary = serializers.CharField(max_length=300, source='description', required=False)

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        gathering = models.Gathering.objects.create(**validated_data)
        for author in authors:
            gathering.authors.add(author)
        return gathering


class SessionSerializer(serializers.Serializer):
    airtableID = serializers.CharField(max_length=20)
    DateofSession = serializers.DateField(source='date')
    Attendance = serializers.SlugRelatedField(many=True, slug_field='airtableID',
                                              queryset=models.Person.objects.all(), source='attendees')
    Class = serializers.SlugRelatedField(many=True, slug_field='airtableID', source='gathering',
                                         queryset=models.Gathering.objects.all())
    Leader = serializers.SlugRelatedField(many=True, slug_field='airtableID', source='leader',
                                          queryset=models.Person.objects.all())

    def create(self, validated_data):
        gathering = validated_data.pop('gathering')
        leaders = validated_data.pop('leader')
        attendees = validated_data.pop('attendees')
        session = models.Session.objects.create(**validated_data)
        session.gathering.add(gathering[0])
        for leader in leaders:
            session.leader.add(leader)
        for attendee in attendees:
            session.attendees.add(attendee)
        return session
