from datetime import datetime
from wrapper.google_calendar import Calendar
from weather import Weather
from deutsche_bahn import Bahn
from google_tasks import Tasks

class Meeting:

    def get_current_time(self):
        return.datetime.now()

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):
        
        """response = {
                "text": "Your next lecture Semantic Web starts in 10 minutes. Remember your \"exam questions\" assignment.",
                "html": "<p>Your next lecture \"Semantic Web\" starts in 10 minutes. Remember your \"exam questions\" assignment. Here is the Zoom link:<p><a href=\"https://dhbw-stuttgart.zoom.us/j/2334403821?pwd=RWpkUjFQSnlZdVEwRDNLTWV0QS9tQT09\">Semantic Web</a>",
                "follow_up": "meeting",
                "context": "test"
            }"""

        return response

    def meeting(self, text, context, preferences):
        calender = Calender("DHBW6")
        events = calendar.get_events_today().json()

        for event in events:
            if event.starts > get_current_time.hour:
                title = event.title
                location = event.location
                start = event.start
                end = event.end
                brake
        
        if "zoom" in event.location:
            response = {
                "text": "Your next appointment is " + title + " from " + start + " to " + end + ". The link will take you to the meeting.",
                "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + ". Zoom-link: " + location + "<p>",
                "follow_up": null,
                "context": null
            }
        
        else:
            weather = Weather(location_weather)
            current_weather = weather.get_current_weather()

            deutsche_bahn = Bahn(train_station)
            depatures = deutsche_bahn.get_next_depatures()

            tasks = Tasks()
            list_id = tasks.get_list_id(title)

            if list_id == "":
                response = {
                "text": "Your next appointment is " + title + " from " + start + " to " + end + " at " + location + "."+ current_weather,
                "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + " at " + location + ". " + current_weather + "<p>",
                "follow_up": null,
                "context": null
                }
            else:
                response = {
                "text": "Your next appointment is " + title + " from " + start + " to " + end + " at " + location + "."+ current_weather,
                "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + " at " + location + ". " + current_weather + "<p>",
                "follow_up": "meeting",
                "context": "get_tasks"
                }


            return response

            

    def get_tasks(self, text, context, preferences):
        task_response = tasks.get_tasks_from_list(title)

