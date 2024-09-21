# ajust_app/forms.py

from django import forms
from .models import Event, Date, Participant, Response

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name']

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

DateFormSet = forms.modelformset_factory(Date, form=DateForm, extra=5, max_num=5)

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['availability']
        widgets = {
            'availability': forms.RadioSelect,
        }

ResponseFormSet = forms.modelformset_factory(Response, form=ResponseForm, extra=0)