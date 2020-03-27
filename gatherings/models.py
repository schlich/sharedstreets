from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from recurrence.fields import RecurrenceField
# from schedule.models import Event
from datetime import datetime


GATHERING_TYPES = [
    # ('BS', 'Bible Study'),
    # ('SR', 'Sex and Relationships'),
    # ('ME', 'Movies and Entertainment'),
    # ('PO', 'Political'),
    ('EV', 'Event'),
    ('CL', 'Class'),
    ('GR', 'Group'),
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
    airtableID = models.CharField(max_length=50, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    pronouns = models.CharField(max_length=20, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    leadership_interested = models.BooleanField(null=True)
    leadership_trained = models.BooleanField(null=True)
    connection = models.CharField(max_length=40, choices=CONNECTION_LEVELS, null=True, blank=True)
    participation = models.CharField(max_length=40, choices=PARTICIPATION_LEVELS, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Gathering(models.Model):
#     airtableID = models.CharField(max_length=20, blank=True, null=True)
    # event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True, related_name='gathering')
    name = models.CharField(max_length=50)
    description = models.TextField()
    recurrences = RecurrenceField(null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=2, choices=GATHERING_TYPES)
    authors = models.ManyToManyField(Person)

    @property
    def Date(self):
        return self.recurrences.after(datetime.now())
    
    @property
    def recurrence_text(self):
        return " + ".join([rule.to_text() for rule in self.recurrences.rrules])

    def __str__(self):
        return self.name


# class EventGrouper(models.Model):
#     event = models.OneToOneField(Event)
#     gathering = models.ForeignKey(Gathering,on_delete=models.CASCADE)


class Session(models.Model):
    airtableID = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    leader = models.ManyToManyField(Person, related_name='sessions_lead')
    attendees = models.ManyToManyField(Person, related_name='sessions_attended', blank=True)
    gathering = models.ForeignKey(Gathering, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.gathering.name + ' ' + self.date.strftime('%m/%d/%y')