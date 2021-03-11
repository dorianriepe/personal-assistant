from datetime import datetime
from wrapper.google_calendar import Calendar
from weather import Weather
from deutsche_bahn import Bahn
from google_tasks import Tasks
from html_response import HTMLResponseBuilder

class Meeting:

    def get_current_time(self):
        return.datetime.now()

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):

        if context == "get_tasks":
            response = self.get_tasks(text, preferences)
        else:
            response = self.meeting(text, preferences)
        
        """response = {
                "text": "Your next lecture Semantic Web starts in 10 minutes. Remember your \"exam questions\" assignment.",
                "html": "<p>Your next lecture \"Semantic Web\" starts in 10 minutes. Remember your \"exam questions\" assignment. Here is the Zoom link:<p><a href=\"https://dhbw-stuttgart.zoom.us/j/2334403821?pwd=RWpkUjFQSnlZdVEwRDNLTWV0QS9tQT09\">Semantic Web</a>",
                "follow_up": "meeting",
                "context": "test"
            }"""

        return response

    def meeting(self, text, preferences):
        calender = Calender("DHBW6")
        events = calendar.get_events_today().json()

        if len(events) > 0:
            title = events[0].title
            location = events[0].location
            start = events[0].start
            end = events[0].end
        else:
            response = {
                "text": "You don't have any appointments today.",
                "html": "<p>You don't have any appointments today."<p>",
                "follow_up": None,
                "context": None
            }

            return response

        """for event in events:
            if event.starts > get_current_time.hour:
                title = event.title
                location = event.location
                start = event.start
                end = event.end
                brake

            else 
                response = {
                "text": "You don't have any appointments today.",
                "html": "<p>You don't have any appointments today."<p>",
                "follow_up": None,
                "context": None
            }

            return response"""

        tasks = Tasks()
        list_id = tasks.get_list_id(title)
        
        if "zoom" in event.location:
            if list_id = "":
                response = {
                    "text": "Your next appointment is " + title + " from " + start + " to " + end + ". The link will take you to the meeting.",
                    "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + ". Zoom-link: " + location + "<p>",
                    "follow_up": None,
                    "context": None
                }
            else:
                response = {
                    "text": "Your next appointment is " + title + " from " + start + " to " + end + ". The link will take you to the meeting. I found a tasklist with the title " + title + ". Do you want me to show you these tasks?",
                    "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + ". Zoom-link: " + location + " I found a tasklist with the title " + title + ". Do you want me to show you these tasks?<p>",
                    "follow_up": "meeting",
                    "context": "get-tasks"
                }
        
        else:
            weather = Weather(preferences.location_weather)
            current_weather = weather.get_current_weather()

            deutsche_bahn = Bahn(preferences.train_station)
            depatures = deutsche_bahn.get_next_depatures()

            depature_html= ""
            
            html_response_builder = HTMLResponseBuilder()

            departure_html = html_response_builder.list_time_title(departure_html, departures)

            """for depature in depatures:
                depature_time = depature.time
                depature_train = depature.train

                depature_html += depature_time + "  -  " + depature_train"\n""""

            

            if list_id == "":
                response = {
                "text": "Your next appointment is " + title + " from " + start + " to " + end + " at " + location + "."+ current_weather + "Here is a list of the next depatures at your train station.",
                "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + " at " + location + ". " + current_weather + "\nDepatures at " + train_station + depature_html + "<p>",
                "follow_up": null,
                "context": null
                }
            else:
                response = {
                "text": "Your next appointment is " + title + " from " + start + " to " + end + " at " + location + "."+ current_weather + "Here is a list of the next depatures at your train station. I found a tasklist with the title " + title + ". Do you want me to show you these tasks?",
                "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + " at " + location + ". " + current_weather + "\nDepatures at " + train_station + depature_html + "I found a tasklist with the title " + title + ". Do you want me to show you these tasks?<p>",
                "follow_up": "meeting",
                "context": "get_tasks"
                }


            return response

            

    def get_tasks(self, text, preferences):
        events = calendar.get_events_today().json()
        if len(events) > 0:
            title = events[0].title
        else:
            response = {
                "text": "Sorry something went wrong.",
                "html": "<p>Sorry something went wrong."<p>",
                "follow_up": None,
                "context": None
            }

            return response
        
        tasks = Tasks()
        task_response = tasks.get_tasks_from_list(title)

        response = {
                "text": "Here are you're tasks." + task_response,
                "html": "<p>Tasks:\n"+ task_response "<p>",
                "follow_up": None,
                "context": None
            }

            return response

