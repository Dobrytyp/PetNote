import json
# import requests

# django imports
from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# # app imports
from .models import GCalEntry

# google calendar api imports
from googleapiclient import discovery
from oauth2client import tools
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
import httplib2

# Create your views here.


class EventList(ListView):
    model = GCalEntry


class EventDetail(DetailView):
    model = GCalEntry


class EventCreate(CreateView):
    model = GCalEntry
    fields = '__all__'


class EventUpdate(UpdateView):
    model = GCalEntry
    fields = '__all__'


class EventDelete(DeleteView):
    model = GCalEntry
    success_url = reverse_lazy('gcal:event-list')

# ---------------------------------------------------------------------------
# google_calendar_connection
# ---------------------------------------------------------------------------


# with open('gcal_credentials/client_secret.json', 'r') as f:
#     gc_id = json.load(f)
    # print(gc_id)


def google_calendar_connection():
    """
    This method used for connect with google calendar api.
    """

    flags = tools.argparser.parse_args([])
    FLOW = OAuth2WebServerFlow(
        client_id=gc_id['web']['client_id'],
        client_secret=gc_id['web']['client_secret'],
        scope='https://www.googleapis.com/auth/calendar',
        user_agent='PetNote'
    )

    storage = Storage('calendar.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid == True:
        credentials = tools.run_flow(FLOW, storage, flags)

    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = discovery.build('calendar', 'v3', http=http)

    return service


def gcal(request):
    return render(request, 'gcal/event_list.html')
