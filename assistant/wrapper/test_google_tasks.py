import unittest
from unittest.mock import patch

from datetime import datetime
from google_tasks import Tasks

class Testing(unittest.TestCase):
    
    def test_get_list_id(self):
        
        tasks = Tasks()

        response = tasks.get_list_id("Test Google Tasks")
        list_id = "VEhDejNacGU1NTNyb09RZg"

        self.assertEqual(response, list_id)
    
    def test_get_tasks(self):
        
        tasks = Tasks()

        response = tasks.get_tasks("VEhDejNacGU1NTNyb09RZg")
        response_exp = {'kind': 'tasks#tasks', 'etag': '\"LTgzODU3NDY5NQ\"'}

        self.assertEqual(response, response_exp)
    
    
    @patch('google_tasks.Tasks.get_tasks')
    def test_todays_events(self, mock__get_response):

        mock__get_response.return_value = {'kind': 'tasks#tasks', 'etag': '"LTg3MzE0MDkyOQ"'}

        tasks = Tasks()
        response = tasks.get_tasks_from_list("Einkaufen")

        self.assertEqual(response, [])
    

if __name__ == '__main__':
    unittest.main()
