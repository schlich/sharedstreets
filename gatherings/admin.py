from django.contrib import admin

# Register your models here.
from .models import Session, Gathering

admin.site.register(Session)
admin.site.register(Gathering)

#
