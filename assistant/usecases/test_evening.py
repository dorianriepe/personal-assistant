import unittest
from unittest import TestCase
from unittest.mock import patch
import json
import os
import re

from evening import Evening


class TestEvening(TestCase):

    def __init__(self):
        super().__init__()

        # set preferences for every method
        self.preferences = {'news': 'https://rss.dw.com/rdf/rss-en-ger', 'name': 'Jan', 'location': 'Stuttgart',
                            'liga': '1.Bundesliga', 'club': 'Bayern', 'diet': 'balanced', 'health': 'alcohol-free'}
        # initialize a cooking use case instance
        self.instance = Evening()
    
    @patch('bundesliga.Bundesliga.get_bundesliga_results')
    @patch('google_calendar.Calendar.get_first_event_tomorrow')
    def goodEvening(self):
        with open('test_response_bundesliga_results.json', 'r') as file:
            data = file.read()
        with open('test_response_calendar.json', 'r') as file:
            data2 = file.read()

        mock_get_bundesliga_results.return_value = data
        mock_get_first_event_tomorrow.return_value = data2

        response = self.instance.handle(None, None , self.preferences)
        expected_response_regex = """{'text': 'Good evening. Stuttgart played 1-2 against Dortmund. Do you want to see the current standings?', 'html': '<p>Good evening. Stuttgart played 1-2 against Dortmund. Do you want to see the current standings?</p>', 'follow_up': 'evening', 'context': 'bundesliga'}"""

        self.assertTrue(re.match(expected_response_regex, response))

    @patch('html_response.HTMLResponseBuilder.rank_image_name')
    def test_bundesligaTable(self,  mock__requests_get):
        with open('test_response_bundesliga.htmltxt', 'r') as file:
            data = file.read()

        mock_rank_image_name.return_value = data
        response = self.instance.handle("Yes please show me the standings", "bundesliga" , self.preferences)
        
        expected_response_regex = """{'text': 'Here is the current league table. Should I give you a weather forecast for tomorrow?', 'html': '%s', 'follow_up': 'evening', 'context': 'playlist'}""" % data

        self.assertTrue(re.match(expected_response_regex, response))
    
    def test_spotify(self):
        response = self.instance.handle("Yes, can you give me a sleeping playlist?", "spotify", self.preferences)
        expected_response_regex = """{'text': "I found this playlist. Do you want me to start the playlist?", 'html': '<p>.*</p><div class="img-title-subtitle">.*</div>', 'follow_up': 'evening', 'context': 'playSpotify.*'}"""

        self.assertTrue(re.match(expected_response_regex, response))

    def test_playSpotify(self):
        response = self.instance.handle("Yes, please start this playlist.", "playSpotify")
        expected_response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        self.assertEqual(expected_response, response)

if __name__ == '__main__':
    unittest.main()
