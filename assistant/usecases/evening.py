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
        calendar = Calendar("DHBW6")
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
            bundesliga = Bundesliga(preferences["league"])
            spieltag = bundesliga.get_bundesliga_results()
            spiel = spieltag[0]

            speak_spieltag = "The Bundesliga played today. %s played %d to %d against %s. Shall I give you the current standings?" % (
                spiel["team1ShortName"], spiel["toreTeam1"], spiel["toreTeam2"], spiel["team2ShortName"])
            speak_meeting = speak_meeting + " " + speak_spieltag
            context = "bundesliga"

        else:
            speak_weather = "Shall I give you a weather forecast for tomorrow?"
            speak_meeting = speak_meeting + " " + speak_weather
            context = "weather"

        response = {
            "speak": speak_meeting,
            "html": "<p>" + speak_meeting + "<\p>",
            "follow_up": "Evening",
            "context": context
        }
        return response

    def bundesligaTable(self, text, preferences):
        if ("yes" in text):
            bundesliga = Bundesliga(preferences["league"])
            html_builder = HTMLResponseBuilder()
            table = bundesliga.get_table_top_five()
            text = "Here is the current league table, should I also give you a weather forecast for tomorrow?"

            speak_table = "Here is the current league table. "
            for rank in table:
                speak_table = speak_table + " Rank" + \
                    str(rank["rank"]) + rank["clubShortName"] + \
                    " with " + str(rank["Points"]) + " Points"

            speak_table = speak_table + " Should I also give you a weather forecast for tomorrow?"
            html = html_builder.rank_image_name(text, table)

            response = {
                "speak": speak_table,
                "html": html,
                "follow_up": "Evening",
                "context": "weather"
            }
            return response

        else:
            speak_table = " Should I also give you a weather forecast for tomorrow?"
            html = " Should I also give you a weather forecast for tomorrow?"
            response = {
                "speak": speak_table,
                "html": html,
                "follow_up": "Evening",
                "context": "weather"
            }
            return response

    def weatherForecast(self, text, preferences):
        if ("yes" in text):
            weather = Weather(preferences["location"])

            text = weather.get_evening_forecast()
            speak_weather = text + "Would you like to listen to some music to fall asleep?"
            response = {
                "speak": speak_weather,
                "html": "<p>" + speak_weather + "<\p>",
                "follow_up": "Evening",
                "context": "playlist"
            }
            return response

        else:
            speak_weather = "Would you like to listen to some music to fall asleep?"
            response = {
                "speak": speak_weather,
                "html": "<p>" + speak_weather + "<\p>",
                "follow_up": "Evening",
                "context": "playlist"
            }
            return response

    def spotify(self, text, preferences):
        if ("yes" in text):
            spotify = Spotify()
            playlist = spotify.get_playlist("sleep")[0]
            text = "I found a playlist for you. Shall I play it?"

            html = HTMLResponseBuilder.time_title_subtitle(
                text, playlist.title, playlist.author, playlist.image_url, playlist.uri)
            response = {
                "speak": text,
                "html": html,
                "follow_up": "Evening",
                "context": playlist.uri
            }
            return response

        else:
            response = {
                "speak": None,
                "html": None,
                "follow_up": None,
                "context": None
            }
            return response

    def spotifyPlay(self, text, context):
        if ("yes" in text):
            spotify = Spotify()
            spotify.get_device_id("WEB")
            spotify.start_playback(context)

        response = {
            "speak": None,
            "html": None,
            "follow_up": None,
            "context": None
        }
        return response
