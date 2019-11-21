from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from gatherings.models import Gathering, Session


class GatheringForm(ModelForm):
    class Meta:
        model = Gathering
        fields = ['name', 'description', 'category', 'authors']

class SessionForm(ModelForm):
    class Meta:
        model = Session
        exclude = ('gathering',)

SessionFormSet = inlineformset_factory(Gathering, Session, form=SessionForm)