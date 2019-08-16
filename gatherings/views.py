from django.shortcuts import render
from .models import Session
import datetime


def upcoming_sessions(request):
    today = datetime.date.today()
    end = today + datetime.timedelta(days=7)
    upcoming = Session.objects.filter(date__range=[today, end])
    context = {
        'upcoming_sessions': upcoming,
    }
    return render(request, 'gatherings/index.html', context)

