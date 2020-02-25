from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from gatherings.models import Session, Gathering
from gatherings.forms import SessionFormSet
from django.utils import timezone
import datetime


class IndexView(generic.ListView):
    template_name = 'gatherings/index.html'

    model = Gathering

    def get_context_data(self, **kwargs):
        event_list = list(Gathering.objects.all())
        upcoming_events = sorted(event_list, key = lambda event: event.Date)[:5]
        context = super().get_context_data(**kwargs)
        context['upcoming'] = upcoming_events 
        return context
    # def get_queryset(self):

    #     return Event.objects.all()

# class QuarterGatherings(generic.ListView):
#     template_name = 'gatherings/quarter.html'



class AllGatherings(generic.ListView):
    model = Gathering
    template_name = "gatherings/list.html"

# class GatheringView(FormView):
#     template_name = 'add.html'
#     form_class = GatheringForm
#     success_url = '../'

class GatheringCreate(CreateView):
    model = Gathering
    fields = ['name','description','category','authors']
    

class GatheringSessionCreate(CreateView):
    model = Gathering
    def get_context_data(self, **kwargs):
        data = super(GatheringSessionCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['sessions'] = SessionFormSet(self.request.POST)
        else:
            data['sessions'] = SessionFormSet()
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        sessions = context['sessions']
        with transaction.atomic():
            self.object = form.save()

            if sessions.is_valid():
                sessions.instance = self.object
                sessions.save()
        return super(GatheringSessionCreate, self).form_valid(form)


class GatheringUpdate(UpdateView):
    model = Gathering
    fields = ['name','description','category','authors']


class GatheringDelete(DeleteView):
    model = Gathering
    success_url = reverse_lazy('author-list')

# class Session
