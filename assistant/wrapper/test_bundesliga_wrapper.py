from bundesliga import Bundesliga
import unittest
from unittest.mock import patch
import json
import os


class TestBundesligaWrapper(unittest.TestCase):

    @patch('bundesliga.Bundesliga.get_requests')
    def test_get_clubs(self, mock__requests_get):
        bundesliga = Bundesliga(1)
        test_path = os.path.join(
            "test-responses-bundesliga", "clubs_response.json")
        exp_res_path = os.path.join(
            "test-responses-bundesliga", "clubs_exp_response.json")
        exp_res_json = json.loads(open(exp_res_path, "r").read())
        test_json = json.loads(open(test_path, "r").read())
        mock__requests_get.return_value = test_json

        response = bundesliga.get_clubs()
        self.assertEqual(response, exp_res_json)

    @patch('bundesliga.Bundesliga.get_requests')
    def test_get_bundesliga_results(self, mock__requests_get):
        bundesliga = Bundesliga(1)
        test_path = os.path.join(
            "test-responses-bundesliga", "results_response.json")
        exp_res_path = os.path.join(
            "test-responses-bundesliga", "results_exp_response.json")
        exp_res_json = json.loads(open(exp_res_path, "r").read())
        test_json = json.loads(open(test_path, "r").read())
        mock__requests_get.return_value = test_json

        response = bundesliga.get_bundesliga_results()
        self.assertEqual(response, exp_res_json)

    @patch('bundesliga.Bundesliga.get_requests')
    def test_get_table_top_five(self, mock__requests_get):
        bundesliga = Bundesliga(1)
        test_path = os.path.join(
            "test-responses-bundesliga", "top_five_response.json")
        exp_res_path = os.path.join(
            "test-responses-bundesliga", "top_five_exp_response.json")
        exp_res_json = json.loads(open(exp_res_path, "r").read())
        test_json = json.loads(open(test_path, "r").read())
        mock__requests_get.return_value = test_json

        response = bundesliga.get_table_top_five()
        self.assertEqual(response, exp_res_json)


if __name__ == '__main__':
    unittest.main()
