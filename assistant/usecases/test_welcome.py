import unittest
from unittest import TestCase
from unittest.mock import patch
import json
import os
import re

from usecases.welcome import Welcome


class TestWelcome(TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)

        self.preferences = {'name': 'Jürgen', 'location': 'Stuttgart'}
        self.instance = Welcome()

    def test_workout(self):
        response = self.instance.handle("Yes", "workout", self.preferences)
        self.assertTrue(re.match('\.*Ok\. Should I start the playlist on Spotify.*context.*spotify.*', response))

    def test_play_spotify(self):
        response = self.instance.handle(
            "Yes, please start this playlist.", "spotify", self.preferences)

        expected_response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        self.assertEqual(expected_response, response)

    def test_good_morning(self):
        response = self.instance.handle(
            None, "proactiveWelcome", self.preferences)

        self.assertTrue(re.match('\.*Good morning Jürgen.*Today you have.*Do you want to start a workout and listen to some music.*context.*workout.*', response))


if __name__ == '__main__':
    unittest.main()
