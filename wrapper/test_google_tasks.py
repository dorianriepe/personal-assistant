import unittest
from unittest.mock import patch

from datetime import datetime
from google_tasks import Tasks

class Testing(unittest.TestCase):
    
    def test_get_list_id(self):
        
        tasks = Tasks()

        response = tasks._get_list_id("Einkaufen")
        list_id = "eVp3NkZtSm9mWk5ydGxRcw"

        self.assertEqual(response, list_id)
    
    def test__get_tasks(self):
        
        tasks = Tasks()

        response = tasks._get_tasks("eVp3NkZtSm9mWk5ydGxRcw")
        response_exp = {'kind': 'tasks#tasks', 'etag': '\"LTg3MzE0MDkyOQ\"'}

        self.assertEqual(response, response_exp)
    
    '''
    @patch('google_tasks.Tasks._get_events_for_day')
    def test_todays_events(self, mock__get_response):

        mock__get_response.return_value = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        google_calendar = Calendar("DHBW6")
        events = google_calendar.get_events_today()

        response = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        self.assertEqual(events, response)
    '''

if __name__ == '__main__':
    unittest.main()
