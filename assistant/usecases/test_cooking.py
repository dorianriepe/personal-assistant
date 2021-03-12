import unittest
from unittest import TestCase
from unittest.mock import patch
import json
import os

from cooking import Cooking


class TestCooking(TestCase):

    def test_cookNow(self):
        inst = Cooking()
        preferences = {"Name": "Philip"}
        response = inst.handle("i'm hungry", None, preferences)

        expected_response = {}

        self.assertEqual(expected_response, response)
