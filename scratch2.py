# coding: utf-8
from gatherings.serializers import PersonSerializer
person = people[0]
fields = person['fields']
fields = {k.translate({32:None}) : v for k, v in fields.items()}
fields = {k.replace('?',''): v for k, v in fields.items()}
serializer = PersonSerializer(data=fields)
