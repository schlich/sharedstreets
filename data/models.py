from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

CONNECTION_LEVELS = [
    (1, 'Acknowledgement'),
    (2, 'Dialogue/Emotional Connection'),
    (3, 'Intersection'),
    (4, 'Invitation'),
]
PARTICIPATION_LEVELS = [
    (1, 'Connection'),
    (2, 'Contact'),
    (3, 'Visitor'),
    (4, 'Participant'),
]
GATHERING_CATEGORIES = [
    ('BS', 'Bible Study'),
    ('SR', 'Sex and Relationships'),
    ('ME', 'Movies and Entertainment'),
]

class Person(models.Model()):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    pronouns = models.CharField(max_length=20)
    phone = PhoneNumberField()
    email = models.EmailField()
    birthday = models.DateField()
    leadership_interested = models.BinaryField()
    leadership_trained = models.BinaryField()
    connection = models.IntegerField(choices=CONNECTION_LEVELS)
    participation = models.IntegerField(choices=PARTICIPATION_LEVELS)


class Gathering(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=2, choices=GATHERING_CATEGORIES)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)


class Session(models.Model):
    date = models.DateField()
    gathering = models.ForeignKey(Gathering, on_delete=models.CASCADE)
    leader = models.ForeignKey(Person, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(Person)

