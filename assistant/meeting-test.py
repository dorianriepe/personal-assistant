import unittest
from unittest import TestCase
from unittest.mock import patch
import json

from usecases.meeting import Meeting

class TestMeeting(TestCase):

    def __init__(self):
        super().__init__()

        # set preferences for every method
        self.preferences = {'news': 'https://rss.dw.com/rdf/rss-en-ger', 'name': 'Philip', 'location': 'Stuttgart',
                            'liga': '1.Bundesliga', 'club': 'Bayern', 'diet': 'balanced', 'health': 'alcohol-free'}
        # initialize a cooking use case instance
        self.instance = Meeting()

    @patch('google_calendar.Calendar.get_events_today')
    def test_meeting(self, mock__get_response):

        mock__get_response.return_value = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        response = self.instance.handle("what is my next meeting", None, self.preferences)

        suppossed_response= {
                "text": "Your next lecture is Datenbanken starting at 10:00. The link will take you to the zoom meeting.",
                "html": html,
                "follow_up": follow_up,
                "context": context
            }

    @patch('google_calendar.Calendar.get_events_today')
    def test_get_tasks(self, mock__get_response):

        mock__get_response.return_value = [{'title': 'Test Google Tasks', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        response = self.instance.handle("yes", "get-tasks", self.preferences)

        suppossed_response = {
            "text": "Here are your tasks: Test Task ",
            "html": "<p>Here are your tasks: Test Task </p>",
            "follow_up": None,
            "context": None

        }

if __name__ == '__main__':
    unittest.main()