from datetime import datetime
from wrapper.google_calendar import Calendar
from wrapper.weather import Weather
from wrapper.deutsche_bahn import Bahn
from wrapper.google_tasks import Tasks
from wrapper.html_response import HTMLResponseBuilder

class Meeting:

    def get_current_time(self):
        return datetime.now()

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):

        if context == "get-tasks":
            response = self.get_tasks(text, preferences)
        else:
            print("handle.meeting")
            response = self.meeting(text, preferences)
        return response

    def meeting(self, text, preferences):
        
        calendar = Calendar("ASWE")
        events = calendar.get_events_today()

        if len(events) > 0:
            title = events[0]["title"]
            location = events[0]["location"]
            start = events[0]["start"]
            end = events[0]["end"]
        else:
            response = {
                "text": "You don't have any appointments today.",
                "html": "<p>You don't have any appointments today.<p>",
                "follow_up": None,
                "context": None
            }
            print("len < 0 ")
            return response

        tasks = Tasks()
        tasks = tasks.get_tasks_from_list(title)

        # if it is an online meeting
        if "zoom" in location:

            # start, end
            text = "Your next lecture is " + title + " starting at " + start + ". The link will take you to the zoom meeting."
            follow_up = None
            context = None

            if len(tasks) > 0:
                text += " I found tasks in your " + title + " to-do list. Do you want me to show you these tasks?"
                follow_up = "meeting"
                context = "get-tasks"

            html_builder = HTMLResponseBuilder()
            html = html_builder.time_title_subtitle(
                    text = text, 
                    title = title, 
                    subtitle = "Zoom Meeting", 
                    from_time = start, 
                    to_time = end, 
                    link = location
                )

            response = {
                "text": text,
                "html": html,
                "follow_up": follow_up,
                "context": context
            }
            
            return response
        
        else:

            weather = Weather(preferences.location_weather)
            current_weather = weather.get_current_weather()

            deutsche_bahn = Bahn(preferences.train_station)
            departures = deutsche_bahn.get_next_depatures()

            departure_html= ""
            
            html_response_builder = HTMLResponseBuilder()

            departure_html = html_response_builder.list_time_title(departure_html, departures)
            
            if len(tasks) == 0:
                response = {
                "text": "Your next appointment is " + title + " from " + start + " to " + end + " at " + location + "."+ current_weather + "Here is a list of the next depatures at your train station.",
                "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + " at " + location + ". " + current_weather + "\nDepatures at " + train_station + depature_html + "<p>",
                "follow_up": None,
                "context": None
                }
            else:
                response = {
                "text": "Your next appointment is " + title + " from " + start + " to " + end + " at " + location + "."+ current_weather + "Here is a list of the next depatures at your train station. I found a tasklist with the title " + title + ". Do you want me to show you these tasks?",
                "html": "<p>Your next appointment is " + title + " from " + start + " to " + end + " at " + location + ". " + current_weather + "\nDepatures at " + train_station + depature_html + "I found a tasklist with the title " + title + ". Do you want me to show you these tasks?</p>",
                "follow_up": "meeting",
                "context": "get_tasks"
                }

            return response

            

    def get_tasks(self, text, preferences):
        
        negative_text = ['no', 'dont']
        if any(t in text for t in negative_text):
            response = {
                "text": None,
                "html": None,
                "follow_up": None,
                "context": None
            }
            return response

        calendar = Calendar("ASWE")
        events = calendar.get_events_today()
        
        if len(events) > 0:
            title = events[0]["title"]
        
        else:
            response = {
                "text": "Sorry something went wrong.",
                "html": "<p>Sorry something went wrong.</p>",
                "follow_up": None,
                "context": None
            }
            return response
        
        tasks = Tasks()
        response = tasks.get_tasks_from_list(title)

        text = "Here are your tasks: "
        html = "<p>Here are your tasks: "

        for task in response:
            text += task + " "
            html += task + " "

        html += "</p>"


        response = {
                "text": text,
                "html": html,
                "follow_up": None,
                "context": None
            }

        return response