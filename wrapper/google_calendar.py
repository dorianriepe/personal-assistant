import os
import pickle
from datetime import datetime, timedelta
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


class Calendar:

    def __init__(self, name):
        
        if not os.path.isfile("./credentials.pkl"):
            
            if os.path.isfile("./client-secret.json"):
                flow = InstalledAppFlow.from_client_secrets_file("client-secret.json", scopes=['https://www.googleapis.com/auth/calendar'])
                credentials = flow.run_console()
                pickle.dump(credentials, open("credentials.pkl", "wb"))
            
            else:
                raise FileNotFoundError("Secrets file (./client-secret.json) not found")
        
        else:
            credentials = pickle.load(open("credentials.pkl", "rb"))
        
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

    def get_events_today(self):
        
        now = datetime.now()
        
        time_min = now.replace(hour=00, minute=00, second=00)
        time_max = now.replace(hour=23, minute=59, second=59)
        
        time_min = time_min.strftime("%Y-%m-%dT%H:%M:%SZ")
        time_max = time_max.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        response = self.service.events().list(calendarId=self.calendar_id, timeMin=time_min, timeMax=time_max).execute()

        events = []

        for event in response["items"]:

            try:
                event_start = datetime.strptime(event["start"]["dateTime"], '%Y-%m-%dT%H:%M:%S%z')
                event_end = datetime.strptime(event["end"]["dateTime"], '%Y-%m-%dT%H:%M:%S%z')
            except KeyError:
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

    def get_first_event_tomorrow(self):
        
        now = datetime.now() + timedelta(days=1)
        
        time_min = now.replace(hour=00, minute=00, second=00)
        time_max = now.replace(hour=23, minute=59, second=59)
        
        time_min = time_min.strftime("%Y-%m-%dT%H:%M:%SZ")
        time_max = time_max.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        response = self.service.events().list(calendarId=self.calendar_id, timeMin=time_min, timeMax=time_max).execute()

        events = []

        for event in response["items"]:

            try:
                event_start = datetime.strptime(event["start"]["dateTime"], '%Y-%m-%dT%H:%M:%S%z')
                event_end = datetime.strptime(event["end"]["dateTime"], '%Y-%m-%dT%H:%M:%S%z')
            except KeyError:
                continue

            event_start = event_start.strftime("%H:%M")
            event_end = event_end.strftime("%H:%M")

            title = event["summary"]
            if "location" in event:
                location = event["location"]
            else: 
                location = ""

            events.append({"title": title, "location": location, "start": event_start, "end": event_end})

        if len(events) > 0:
            return events[0]
        else:
            return {}