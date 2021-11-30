from django import forms
from .models import Bookings, Events

EVENT_TYPE = [
    ('conference', "Conference"),
    ('marriage', "Marriage"),
    ('Birthday', "Birthday"),
    ('Casual_Party', "Casual Party"),
    ('office', "Office Events")
]


allmy = Events.objects.get(event_id=1)
sls = allmy.av_slots
caps = allmy.cap
servs = allmy.serv
Slots = [(x, x) for x in sls.split(',')]
SERVICES = [(x, x) for x in servs.split(',')]

CAPACITY = [(x, x) for x in caps.split(',')]


class BookEvent(forms.Form):
    slots = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=Slots)
    event_type = forms.CharField(
        max_length=150, label="Event Type", widget=forms.Select(choices=EVENT_TYPE))
    capacity = forms.IntegerField(
        label="No. of People", widget=forms.Select(choices=CAPACITY))
    services = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=SERVICES)
    date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class EditEvent(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = Bookings
        fields = ('slots', 'event_type', 'capacity', 'services', 'date')
        widgets = {
            'slots':  forms.CheckboxSelectMultiple(choices=Slots),
            'event_type': forms.Select(choices=EVENT_TYPE),
            'capacity': forms.Select(choices=CAPACITY),
            'services': forms.CheckboxSelectMultiple(choices=SERVICES),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
