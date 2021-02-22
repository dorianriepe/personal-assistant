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
    
    
    @patch('google_tasks.Tasks._get_tasks')
    def test_todays_events(self, mock__get_response):

        mock__get_response.return_value = {'kind': 'tasks#tasks', 'etag': '"LTg3MzE0MDkyOQ"'}

        tasks = Tasks()
        response = tasks.get_tasks_from_list("Einkaufen")

        self.assertEqual(response, [])
    

if __name__ == '__main__':
    unittest.main()
