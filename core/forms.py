from django import forms
from events.models import Event
from django.contrib.auth.models import User
from users.models import UserProfile

class AddEventForm(forms.ModelForm):
    """
    This form is used to add/edit events

    """
    class Meta:
        model = Event
        exclude=('events_logo','questions','tags','category','updates',)

class AddCoordForm(forms.ModelForm):
    """
    This form is used to add/edit coords

    """
    event= forms.ModelChoiceField(queryset=Event.objects.all(),empty_label='----------')

    class Meta:
        model = User
        fields=('username', 'email')

