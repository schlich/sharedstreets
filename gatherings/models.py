from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


GATHERING_CATEGORIES = [
    ('BS', 'Bible Study'),
    ('SR', 'Sex and Relationships'),
    ('ME', 'Movies and Entertainment'),
    ('PO', 'Political'),
]
CONNECTION_LEVELS = [
    ('1-Acknowledgement', 'Acknowledgement'),
    ('2-Dialogue/Emotional Connection', 'Dialogue/Emotional Connection'),
    ('3-Intersection', 'Intersection'),
    ('4-Invitation', 'Invitation'),
]

PARTICIPATION_LEVELS = [
    ('1-Connection', 'Connection'),
    ('2-Contact', 'Contact'),
    ('3-Visitor', 'Visitor'),
    ('4-Participant', 'Participant'),
    ('5-Potential Leader', 'Potential Leader'),
    ('6-Leader', 'Leader'),
    ('7-Leader-Trainer', 'Leader-Trainer'),
]


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    pronouns = models.CharField(max_length=20)
    phone = PhoneNumberField()
    email = models.EmailField()
    birthday = models.DateField(null=True)
    leadership_interested = models.BooleanField(null=True)
    leadership_trained = models.BooleanField(null=True)
    connection = models.CharField(max_length=40, choices=CONNECTION_LEVELS)
    participation = models.CharField(max_length=40, choices=PARTICIPATION_LEVELS)


class Gathering(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=2, choices=GATHERING_CATEGORIES)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)


class Session(models.Model):
    date = models.DateField()
    gathering = models.ForeignKey(Gathering, on_delete=models.CASCADE)
    leader = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='leader')
    attendees = models.ManyToManyField(Person, related_name='attendees')
