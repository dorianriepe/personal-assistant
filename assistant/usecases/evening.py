from wrapper.google_calendar import Calendar
from wrapper.spotify import Spotify
from wrapper.bundesliga import Bundesliga
from wrapper.weather import Weather
from wrapper.html_response import HTMLResponseBuilder
import datetime


class Evening:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):

        if (context == None):
            response = self.goodEvening(preferences)
        elif (context == "bundesliga"):
            response = self.bundesligaTable(text, preferences)
        elif (context == "weather"):
            response = self.weatherForecast(text, preferences)
        elif (context == "playlist"):
            response = self.spotify(text, preferences)
        elif ("spotify" in context):
            response = self.spotifyPlay(text, context)
        else:
            response = self.goodEvening(preferences)

        return response

    def goodEvening(self, preferences):

        # get whether there is a meeting the next day
        calendar = Calendar("ASWE")
        first_meeting = calendar.get_first_event_tomorrow()
        if first_meeting:
            now = datetime.datetime.now()
            format = '%Y-%m-%dT%H:%M:%S%z'
            start = datetime.datetime.strptime(first_meeting["start"], format)
            diff = start - now
            diff = int(diff.seconds)

            # is it 9 hours until the first meeting starts
            # 8h50min: 31800 / 9h10min: 33000
            if diff < 33000 and diff > 31800:
                speak_meeting = "Good evening, you have a meeting tomorrow morning, you should go to sleep soon to get 9 hours of sleep."
                context = "meeting"
            else:
                speak_meeting = "Good evening."
                context = "meeting"
        else:
            speak_meeting = "Good evening."
            context = "meeting"

        # check if bundesliga match day
        weekday = datetime.datetime.today().weekday()
        if weekday == 5 or weekday == 6:

            liga = preferences.get("liga", "1.Bundesliga")
            if "1" in liga:
                liga = 1
            elif "2" in liga:
                liga = 2
            bundesliga = Bundesliga(liga)
            spieltag = bundesliga.get_bundesliga_results()
            spiel = spieltag[0]

            fav_team = preferences.get("club", "Dortmund")
            for spiel in spieltag:
                if spiel["team1ShortName"] == fav_team or spiel["team1ShortName"] == fav_team:
                    speak_spieltag = spiel["team1ShortName"] + " played " + str(spiel["toreTeam1"])+"-"+str(spiel["toreTeam2"])+" against "+spiel["team2ShortName"]+". "
            speak_spieltag += " Do you want to see the current standings?"
            speak_meeting = speak_meeting + " " + speak_spieltag
            context = "bundesliga"

        else:
            speak_weather = "Shall I give you a weather forecast for tomorrow?"
            speak_meeting = speak_meeting + " " + speak_weather
            context = "weather"

        response = {
            "text": speak_meeting,
            "html": "<p>" + speak_meeting + "</p>",
            "follow_up": "evening",
            "context": context
        }
        return response

    def bundesligaTable(self, text, preferences):
        
        if ("yes" in text):
            liga = preferences.get("liga", "1.Bundesliga")
            if "1" in liga:
                liga = 1
            elif "2" in liga:
                liga = 2
            bundesliga = Bundesliga(liga)
            html_builder = HTMLResponseBuilder()
            table = bundesliga.get_table_top_five()
            text = "Here is the current league table, should I also give you a weather forecast for tomorrow?"

            speak_table = "Here is the current league table. "
            for rank in table:
                if rank["rank"] < 3:
                    speak_table += "On rank" + str(rank["rank"]) + " is " + rank["clubShortName"] + " with " + str(rank["points"]) + " points, "
                if rank["rank"] == 3:
                    speak_table += "On rank" + str(rank["rank"]) + " is " + rank["clubShortName"] + " with " + str(rank["points"]) + " points. "
                if rank["rank"] == 4:
                    speak_table += rank["clubShortName"] + " is on rank " + str(rank["rank"]) + " and "
                if rank["rank"] == 5:
                    speak_table += rank["clubShortName"] + " on " + str(rank["rank"]) + ". "
                    

            speak_table = speak_table + " Should I give you a weather forecast for tomorrow?"
            html = html_builder.rank_image_name(text, table)

            response = {
                "text": speak_table,
                "html": html,
                "follow_up": "evening",
                "context": "weather"
            }
            return response

        else:
            text = " Should I give you a weather forecast for tomorrow?"
            response = {
                "text": text,
                "html": "<p>"+text+"</p>",
                "follow_up": "evening",
                "context": "weather"
            }
            return response

    def weatherForecast(self, text, preferences):
        
        if ("yes" in text):
            
            weather = Weather(preferences["location"])

            text = weather.get_evening_forecast()
            text += "Would you like to listen to some music to fall asleep?"
            response = {
                "text": text,
                "html": "<p>" + text + "</p>",
                "follow_up": "evening",
                "context": "playlist"
            }
            return response

        else:
            text = "Would you like to listen to some music to fall asleep?"
            response = {
                "text": text,
                "html": "<p>" + text + "</p>",
                "follow_up": "evening",
                "context": "playlist"
            }
            return response

    def spotify(self, text, preferences):
        if ("yes" in text):
            spotify = Spotify()
            playlist = spotify.get_playlist("sleep")[0]
            text = "I found a playlist for you. Shall I play it?"

            html_response = HTMLResponseBuilder()
            html = html_response.img_title_subtitle(
                    text = text, 
                    title = playlist["name"], 
                    subtitle = playlist["author"], 
                    image_url = playlist["image_url"], 
                    link = playlist["uri"]
                )

            response = {
                "text": text,
                "html": html,
                "follow_up": "evening",
                "context": playlist["uri"]
            }
            return response

        else:
            response = {
                "text": None,
                "html": None,
                "follow_up": None,
                "context": None
            }
            return response

    def spotifyPlay(self, text, context):
        if ("yes" in text):

            spotify = Spotify()
            spotify.start_playback(context)

        response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }
        
        return response
