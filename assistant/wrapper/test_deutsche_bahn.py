import unittest
from unittest.mock import patch

from datetime import datetime
from deutsche_bahn import Bahn

class Testing(unittest.TestCase):
    
    def test_get_station_id(self):
        
        b = Bahn("Goldberg")
        station_id = b.get_station_id("Goldberg")
        
        expected_station_id = "8005201"

        self.assertEqual(station_id, expected_station_id)

    @patch('deutsche_bahn.Bahn.get_departures_for_time')
    def test_get_next_departures(self, mock__get_response):

        mock__get_response.return_value = [{'time': '13:42', 'train': 'S1 Herrenberg'}, {'time': '13:32', 'train': 'S1 Kirchheim(Teck)'}, {'time': '13:47', 'train': 'S1 Plochingen'}, {'time': '13:57', 'train': 'S1 Herrenberg'}, {'time': '13:27', 'train': 'S1 Herrenberg'}]
        b = Bahn("Goldberg")
        next_departures = b.get_next_departures()

        expected_next_departures = [{'time': '13:27', 'train': 'S1 Herrenberg'},{'time': '13:27', 'train': 'S1 Herrenberg'},{'time': '13:32', 'train': 'S1 Kirchheim(Teck)'},{'time': '13:32', 'train': 'S1 Kirchheim(Teck)'},{'time': '13:42', 'train': 'S1 Herrenberg'},{'time': '13:42', 'train': 'S1 Herrenberg'},{'time': '13:47', 'train': 'S1 Plochingen'},{'time': '13:47', 'train': 'S1 Plochingen'},{'time': '13:57', 'train': 'S1 Herrenberg'},{'time': '13:57', 'train': 'S1 Herrenberg'}]
        
        self.assertEqual(next_departures, expected_next_departures)

if __name__ == '__main__':
    unittest.main()