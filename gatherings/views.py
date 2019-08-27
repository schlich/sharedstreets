from django.shortcuts import render
from django.views import generic
from .models import Session
import datetime


class IndexView(generic.ListView):
    template_name = 'gatherings/index.html'
    context_object_name = 'upcoming_gatherings'

    def get_queryset(self):
        today = datetime.date.today()
        end = today + datetime.timedelta(days=7)
        return Session.objects.filter(date__range=[today, end])

# def upcoming_sessions(request):
#     today = datetime.date.today()
#     end = today + datetime.timedelta(days=7)
#     upcoming = Session.objects.filter(date__range=[today, end])
#     context = {
#         'upcoming_sessions': upcoming,
#     }
#     return render(request, 'gatherings/index.html', context)
#
