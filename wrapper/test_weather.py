from datetime import datetime
import os
import json
import unittest
from datetime import datetime
from unittest.mock import patch

from weather_wrapper import Weather

class Testing(unittest.TestCase):

    @patch('weather_wrapper.Weather._get_json_weather')
    def test_get_current_weather(self, mock__get_response):

        response_path = os.path.join("weather-response", "weather.json")
        values = json.loads(open(response_path, "r").read())
        mock__get_response.return_value = values

        w = Weather("Stuttgart")
        response = w.get_current_weather()

        expected_response = "Currently it's Sunny at 15 degrees."

        self.assertEqual(response, expected_response)

    @patch('weather_wrapper.Weather._get_current_time')
    @patch('weather_wrapper.Weather._get_json_weather')
    def test_get_forecast(self, mock__get_response, mock__time_response):

        response_path = os.path.join("weather-response", "weather.json")
        values = json.loads(open(response_path, "r").read())
        mock__get_response.return_value = values
        mock__time_response.return_value = datetime(year=2021, month=2, day=23, hour=14, minute=50)

        w = Weather("Stuttgart")
        response = w.get_forecast()

        expected_response = '15:00Partly cloudy16018:00Partly cloudy16021:00Clear1400:00Clear1203:00Clear1106:00Clear909:00Sunny11012:00Partly cloudy16015:00Sunny19018:00Clear17021:00Clear1400:00Clear1203:00Clear1106:00Clear909:00Sunny12012:00Sunny17015:00Sunny19018:00Sunny17021:00Clear140'

        self.assertEqual(response, expected_response)

    @patch('weather_wrapper.Weather._get_json_weather')
    def test_get_evening_forecast(self, mock__get_response):

        response_path = os.path.join("weather-response", "weather.json")
        values = json.loads(open(response_path, "r").read())
        mock__get_response.return_value = values

        w = Weather("Stuttgart")
        response = w.get_evening_forecast()

        expected_response = "The weather tomorrow morning is Sunny at 11 degrees.\nIn the noon it's Sunny at 19 degrees.\nAt night it's Clear at 14 degrees.\n"

        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
