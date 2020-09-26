# # format import
# from cmath import pi
import json
# from google.protobuf import service
import pickle

# # google calendar api imports
from apiclient.discovery import build
# from oauth2client import tools
# from oauth2client.client import OAuth2WebServerFlow
# from oauth2client.file import Storage
# import httplib2
# from pyasn1.type.char import VisibleString
from google_auth_oauthlib.flow import InstalledAppFlow

# ---------------------------------------------------------------------------
# google_calendar_connection
# ---------------------------------------------------------------------------


with open('gcal_credentials/client_secret.json', 'r') as f:
    gc_id = json.load(f)
    # print(gc_id)

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file(gc_id, scopes=scopes)
credentials = flow.run_console()
pickle.dump(credentials, open('token.pkl', 'wb'))
credentials = pickle.load(open('token.pkl', 'rb'))

service = build('calendar', 'v3', credentials=credentials)


"""
def google_calendar_connection():
    
    # This method used for connect with google calendar api.

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
"""


def get_calendar_list():
    gcal_list = service().calendarList().list().execute()
    return gcal_list


def add_event(visit):
    pass


def edit_even(visit):
    pass


def delete_event(visit):
    pass


def main():
    print(get_cal_list()['items'][0])


if __name__ == '__main__':
    main()
