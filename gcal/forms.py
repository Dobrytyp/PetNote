from pyexpat import model
from django.forms import ModelForm
from .models import GCalEntry


class GCalEntryForm(ModelForm):
    class Meta:
        model = GCalEntry
        fields = [
            'title', 'start_event',
            'end_event', 'all_day', 'repeat_event',
            'notification', 'state', 'privacy',
            'active'
        ]
