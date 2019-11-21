from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from gatherings.models import Session, Gathering
from gatherings.forms import SessionFormSet
import datetime


class IndexView(generic.ListView):
    template_name = 'gatherings/index.html'
    context_object_name = 'upcoming_gatherings'

    def get_queryset(self):
        today = datetime.date.today()
        end = today + datetime.timedelta(days=14)
        return Session.objects.filter(date__range=[today, end]).order_by('date')

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

class Session