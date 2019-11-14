from django.contrib import admin

# Register your models here.
from .models import Session, Gathering, Person

admin.site.register(Session)
admin.site.register(Gathering)
admin.site.register(Person)
#
