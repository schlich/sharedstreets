# Generated by Django 2.2.4 on 2019-08-16 06:50
import requests, phonenumbers
from django.db import migrations
from django.conf import settings
from gatherings.serializers import PersonSerializer

def initialize_from_airtable(apps, schema_editor):
    response = requests.get('https://api.airtable.com/v0/apps7BNP7qTwR1BGF/People',
                            params={'api_key': settings.AIRTABLE_API_KEY})
    records = response.json()
    while True:
        people = records['records']
        for person in people:
            fields = person['fields']
            fields = {k.translate({32: None}): v for k, v in fields.items()}
            fields = {k.replace('?', ''): v for k, v in fields.items()}
            if 'Phone' in fields:
                fields['Phone'] = phonenumbers.format_number(
                    phonenumbers.parse(fields['Phone'], 'US'),
                    phonenumbers.PhoneNumberFormat.E164
                )
            serializer = PersonSerializer(data=fields)
            serializer.is_valid()
            print(serializer.errors)
            serializer.save()
        if 'offset' not in records:
            break
        offset = records['offset']
        response = requests.get('https://api.airtable.com/v0/apps7BNP7qTwR1BGF/People',
                                params={'api_key': settings.AIRTABLE_API_KEY,
                                        'offset': offset})
        records = response.json()


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0006_auto_20190816_0441'),
    ]

    operations = [
        migrations.RunPython(initialize_from_airtable)
    ]
