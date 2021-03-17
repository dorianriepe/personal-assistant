import unittest
from unittest.mock import patch

from datetime import datetime
from google_calendar import Calendar

class Testing(unittest.TestCase):
    
    def test_get_events(self):
        
        today = datetime.now()
        calendar = Calendar("DHBW6")
        events = calendar.get_events_for_day(today)
        
        response = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]
        
        self.assertEqual(events, response)

    @patch('google_calendar.Calendar.get_events_for_day')
    def test_todays_events(self, mock__get_response):

        mock__get_response.return_value = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        google_calendar = Calendar("DHBW6")
        events = google_calendar.get_events_today()

        response = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        self.assertEqual(events, response)

    @patch('google_calendar.Calendar.get_events_for_day')
    def test_tomorrow_event(self, mock__get_response):

        mock__get_response.return_value = [{'title': 'Interaktive Systeme', 'location': '', 'start': '09:00', 'end': '14:00'}]

        google_calendar = Calendar("DHBW6")
        events = google_calendar.get_first_event_tomorrow()

        response = {'title': 'Interaktive Systeme', 'location': '', 'start': '09:00', 'end': '14:00'}

        self.assertEqual(events, response)

if __name__ == '__main__':
    unittest.main()
