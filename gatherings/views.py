from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from gatherings.models import Session, Gathering
# from gatherings.forms import GatheringForm
import datetime


class IndexView(generic.ListView):
    template_name = 'gatherings/index.html'
    context_object_name = 'upcoming_gatherings'

    def get_queryset(self):
        today = datetime.date.today()
        end = today + datetime.timedelta(days=14)
        return Session.objects.filter(date__range=[today, end]).order_by('date')

#
# class GatheringView(FormView):
#     template_name = 'add.html'
#     form_class = GatheringForm
#     success_url = '../'


class GatheringCreate(CreateView):
    model = Gathering
    fields = ['name','description','category','authors']


class GatheringUpdate(UpdateView):
    model = Gathering
    fields = ['name','description','category','authors']


class GatheringDelete(DeleteView):
    model = Gathering
    success_url = reverse_lazy('author-list')
