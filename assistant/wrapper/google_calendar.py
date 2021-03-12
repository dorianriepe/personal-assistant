import os
import pytz
import pickle
from datetime import datetime, timedelta
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


class Calendar:

    def __init__(self, name):
        
        if not os.path.isfile("./calendar-credentials.pkl"):
            
            if os.path.isfile("./calendar-client-secret.json"):
                flow = InstalledAppFlow.from_client_secrets_file("calendar-client-secret.json", scopes=['https://www.googleapis.com/auth/calendar'])
                credentials = flow.run_console()
                pickle.dump(credentials, open("calendar-credentials.pkl", "wb"))
            
            else:
                raise FileNotFoundError("Secrets file (./calendar-client-secret.json) not found")
        
        else:
            credentials = pickle.load(open("calendar-credentials.pkl", "rb"))
        
        service = build("calendar", "v3", credentials=credentials)
        
        response = service.calendarList().list().execute()

        for item in response["items"]:
            if name == item["summary"]:
                calendar_id = item["id"]

        if "calendar_id" not in locals():
            raise NameError("Calendar name is not valid")

        self.name = name
        self.service = service
        self.calendar_id = calendar_id

    def get_events_for_day(self, day):
        
        timzone_berlin = pytz.timezone('Europe/Berlin')
        now = datetime.now(timzone_berlin) # + timedelta(hours = 1)

        time_min = day.replace(hour=00, minute=00, second=00)
        time_max = day.replace(hour=23, minute=59, second=59)
        
        time_min = time_min.strftime("%Y-%m-%dT%H:%M:%SZ")
        time_max = time_max.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        response = self.service.events().list(calendarId=self.calendar_id, timeMin=time_min, timeMax=time_max, timeZone="Europe/Berlin").execute()

        events = []

        for event in response["items"]:

            try:
                event_start = datetime.strptime(event["start"]["dateTime"], '%Y-%m-%dT%H:%M:%S%z')
                event_end = datetime.strptime(event["end"]["dateTime"], '%Y-%m-%dT%H:%M:%S%z')
            except KeyError:
                continue

            if now > event_start:
                continue

            event_start = event_start.strftime("%H:%M")
            event_end = event_end.strftime("%H:%M")

            title = event["summary"]
            if "location" in event:
                location = event["location"]
            else: 
                location = ""

            events.append({"title": title, "location": location, "start": event_start, "end": event_end})
            
        return events 

    def get_events_today(self):
        
        timzone_berlin = pytz.timezone('Europe/Berlin')
        now = datetime.now(timzone_berlin) 
        today = datetime.now()

        events = self.get_events_for_day(today)

        return events

    def get_first_event_tomorrow(self):

        timzone_berlin = pytz.timezone('Europe/Berlin')
        now = datetime.now(timzone_berlin) 
        tomorrow = datetime.now() + timedelta(days=1)

        events = self.get_events_for_day(tomorrow)

        if len(events) > 0:
            return events[0]
        else:
            return {}