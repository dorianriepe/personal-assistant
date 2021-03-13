from datetime import datetime
import os
import json
import unittest
from datetime import datetime
from unittest.mock import patch

from weather import Weather

class Testing(unittest.TestCase):

    @patch('weather.Weather.get_json_weather')
    def test_get_current_weather(self, mock__get_response):

        response_path = os.path.join("weather-response", "weather.json")
        fo = open(response_path, "r")
        values = json.loads(fo.read())
        fo.close()
        mock__get_response.return_value = values

        w = Weather("Stuttgart")
        response = w.get_current_weather()

        expected_response = "Currently it's Sunny at 15 degrees."

        self.assertEqual(response, expected_response)

    @patch('weather.Weather.get_current_time')
    @patch('weather.Weather.get_json_weather')
    def test_get_forecast(self, mock__get_response, mock__time_response):

        response_path = os.path.join("weather-response", "weather.json")
        fo = open(response_path, "r")
        values = json.loads(fo.read())
        fo.close()
        mock__get_response.return_value = values
        mock__time_response.return_value = datetime(year=2021, month=2, day=23, hour=9, minute=00)

        w = Weather("Stuttgart")
        response = w.get_forecast()

        expected_response = "The weather this morning is Sunny at 11 degrees.\n"
        self.assertEqual(response, expected_response)

    @patch('weather.Weather.get_json_weather')
    def test_get_evening_forecast(self, mock__get_response):

        response_path = os.path.join("weather-response", "weather.json")
        fo = open(response_path, "r")
        values = json.loads(fo.read())
        fo.close()
        mock__get_response.return_value = values

        w = Weather("Stuttgart")
        response = w.get_evening_forecast()

        expected_response = "The weather tomorrow morning is Sunny at 11 degrees.\nIn the noon it's Sunny at 19 degrees.\nAt night it's Clear at 14 degrees.\n"

        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
