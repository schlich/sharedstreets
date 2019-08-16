# coding: utf-8
import requests
AT_key = 'keykUFTnmiXwnGg6d'
response = requests.get('https://api.airtable.com/v0/apps7BNP7qTwR1BGF/People', params={'api_key':AT_key})
records = response.json()
people = records['records']
from gatherings.serializers import PersonSerializer
person = people[0]
fields = person['fields']
fields = {k.translate({32:None}) : v for k, v in fields.items()}
fields = {k.replace('?',''): v for k, v in fields.items()}
serializer = PersonSerializer(data=fields)
