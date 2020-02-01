from django.contrib import admin
from .models import Gathering, Person

admin.site.register(Person)
admin.site.register(Gathering)