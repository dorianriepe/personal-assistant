import unittest
from unittest import TestCase
from unittest.mock import patch
import json
import os
import re

from usecases.cooking import Cooking


class TestCooking(TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)

        self.preferences = {'news': 'https://rss.dw.com/rdf/rss-en-ger', 'name': 'Philip', 'location': 'Stuttgart',
                            'liga': '1.Bundesliga', 'club': 'Bayern', 'diet': 'balanced', 'health': 'alcohol-free'}
        self.instance = Cooking()

    def test_cookNow(self):
        response = self.instance.handle("i'm hungry", None, self.preferences)
        expected_response_regex = """{'text': 'Today you.*', 'html': '<p>.*</p><div class="img-title-subtitle">.*</div>', 'follow_up': 'cooking', 'context': 'spotify'}"""

        self.assertTrue(re.match(expected_response_regex, response))

    def test_shoppingList(self):
        response = self.instance.handle(
            None, "proactiveShoopingList", self.preferences)

        expected_response_regex = """{'text': "Today you .*", 'html': "<p>Shall I put the ingredients on the shopping list?</p>", 'follow_up': 'cooking', 'context': 'shoppingList'}"""

        self.assertTrue(re.match(expected_response_regex, response))

    def test_shoppingListResponseHandling(self):
        response = self.instance.handle(
            "Yes, please add the ingredients on my shopping list", "shoppingList", self.preferences)

        expected_response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        self.assertEqual(expected_response, response)

    def test_spotify(self):
        response = self.instance.handle(
            "Yes, can you give me a cooking playlist?", "spotify", self.preferences)

        expected_response_regex = """{'text': "I found this playlist. Do you want me to start the playlist?", 'html': '<p>.*</p><div class="img-title-subtitle">.*</div>', 'follow_up': 'cooking', 'context': 'playSpotify.*'}"""

        self.assertTrue(re.match(expected_response_regex, response))

    def test_playSpotify(self):
        response = self.instance.handle(
            "Yes, please start this playlist.", "playSpotify", self.preferences)

        expected_response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        self.assertEqual(expected_response, response)

    def askForCooking(self):
        response = self.instance.handle(
            None, "proactiveCooking", self.preferences)

        expected_response = {
            "text": "Hey, have you already cooked? If not, would you like to cook now?",
            "html": "<p>Hey, have you already cooked? If not, would you like to cook now?</p>",
            "follow_up": "cooking",
            "context": "cook"
        }

        self.assertEqual(expected_response, response)


if __name__ == '__main__':
    unittest.main()
