import os
import json
import urllib.request
from collections import defaultdict
from datetime import datetime


# Utiliy function to create dictionary 
def multi_dict(K, type): 
    if K == 1: 
        return defaultdict(type) 
    else: 
        return defaultdict(lambda: multi_dict(K-1, type)) 

class Weather:

    def get_current_time(self):
        return datetime.now()

    def get_forecast(self):

        text = ""
        for i, day in enumerate(self.weather_data.values()):

            for hour, hour_data in day.items():
                if i > 0 or self.get_current_time().hour*100 < int(hour):
                    text += str(int(int(hour)/100))+":00"
                    text += hour_data["weatherDesc"]
                    text += hour_data["tempC"]
                    text += hour_data["chanceofrain"]
        text = "Today is good weather."
        return text

    def get_evening_forecast(self):
        text = ""
        tomorrow = list(self.weather_data)[1]
        tomorrow = self.weather_data[tomorrow]

        text += "The weather tomorrow morning is "+tomorrow["900"]["weatherDesc"]+" at "+tomorrow["900"]["tempC"]+" degrees.\n"
        if int(tomorrow["900"]["chanceofrain"]) > 50:
            text += "The chance of rain is about "+tomorrow["900"]["chanceofrain"]+" percent.\n"

        text += "In the noon it's "+tomorrow["1500"]["weatherDesc"]+" at "+tomorrow["1500"]["tempC"]+" degrees.\n"
        if int(tomorrow["1500"]["chanceofrain"]) > 50:
            text += "The chance of rain is about "+tomorrow["1500"]["chanceofrain"]+" percent.\n"

        text += "At night it's "+tomorrow["2100"]["weatherDesc"]+" at "+tomorrow["2100"]["tempC"]+" degrees.\n"
        if int(tomorrow["2100"]["chanceofrain"]) > 50:
            text += "The chance of rain is about "+tomorrow["2100"]["chanceofrain"]+" percent.\n"

        return text

    def get_current_weather(self):
        return "Currently it's "+self.current_weatherDesc+" at "+self.current_temp_C+" degrees."

    def get_json_weather(self, location):
        try:
            url = "http://wttr.in/"+location+"?format=j1"
            response = urllib.request.urlopen(url)
            data = response.read()
            values = json.loads(data)
        except urllib.error.HTTPError:
            response_path = os.path.join("weather-response", "weather.json")
            values = json.loads(open(response_path, "r").read())
        return values

    def _load_weather_data(self, location):
        values = self.get_json_weather(location)

        current_weather = values['current_condition'][0]

        self.current_temp_C = current_weather['temp_C']
        self.current_weatherDesc = current_weather["weatherDesc"][0]["value"]

        for day in values['weather']:

            for hourly in day['hourly']:
                self.weather_data[day["date"]][hourly["time"]]["tempC"]=hourly["tempC"]
                self.weather_data[day["date"]][hourly["time"]]["chanceofrain"]=hourly["chanceofrain"]
                self.weather_data[day["date"]][hourly["time"]]["weatherDesc"]=hourly["weatherDesc"][0]["value"]

    def __init__(self,location):

        # Initialize dictionary 
        self.weather_data={}
        
        # Creating Multidimensional dictionary using defaultdict() 
        self.weather_data = multi_dict(3, str)

        # Load current weather data
        self._load_weather_data(location)
