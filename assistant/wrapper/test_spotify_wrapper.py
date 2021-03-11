import unittest
from unittest.mock import patch
import json
import os

from spotify import Spotify


class TestSpotifyWrapper(unittest.TestCase):

    @patch('spotify.Spotify.get_request')
    def test_get_current_playing(self, mock__get_response):

        spotify = Spotify()

        test_path = os.path.join(
            "test-responses-spotify", "currentPlayingResponse.json")
        exp_res_path = os.path.join(
            "test-responses-spotify", "currentPlayingExpResponse.json")

        exp_res_json = json.loads(open(exp_res_path, "r").read())
        test_json = json.loads(open(test_path, "r").read())
        mock__get_response.return_value = test_json

        response = spotify.get_current_playing()

        self.assertEqual(response, exp_res_json)

    @patch('spotify.Spotify.get_request')
    def test_get_device_id(self, mock__get_response):

        spotify = Spotify()

        test_path = os.path.join(
            "test-responses-spotify", "deviceIdResponse.json")

        test_json = json.loads(open(test_path, "r").read())

        mock__get_response.return_value = test_json

        device = "Connect150SE 305890942ae5"
        spotify.get_device_id(device)

        exp_res = "f5b81d7cf3c22cc1098598b69fcd3f6f52fe8961"
        res = spotify.deviceID
        self.assertEqual(res, exp_res)

    @patch('spotify.Spotify.get_request')
    def test_get_playlist(self, mock__get_response):

        spotify = Spotify()

        test_path = os.path.join("test-responses-spotify", "playlistResponse.json")
 
        exp_res_path = os.path.join("test-responses-spotify", "playlistExpResponse.json")

        exp_res_json = json.loads(open(exp_res_path, "r", encoding='cp850').read())
        test_json = json.loads(open(test_path, "r", encoding='cp850').read())
        mock__get_response.return_value = test_json

        response = spotify.get_playlist("workout")

        self.assertEqual(response, exp_res_json)

if __name__ == '__main__':
    unittest.main()
