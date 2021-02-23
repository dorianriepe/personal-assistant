import json
import requests
import os


class Spotify:
    def __init__(self):
        self.client_id = os.environ.get('SPOTIFY_CLIENT_ID')
        self.client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.token = os.environ.get('SPOTIFY_TOKEN')
        self.refresh_token = os.environ.get('SPOTIFY_REFRESH_TOKEN')
        self.api_url = "https://api.spotify.com"

    def request_new_token(self):
        # REQUEST NEW TOKEN:
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }
        response = requests.post(
            'https://accounts.spotify.com/api/token', data=data)

        # GET TOKEN:
        response = response.json()
        self.token = response["access_token"]

    def get_request(self, endpoint):
        response = requests.get(self.api_url+endpoint, headers={"Accept": "application/json", "Content-Type": "application/json",
                                                                "Authorization": "Bearer " + self.token})
        status_code = response.status_code
        if status_code == 401:
            self.request_new_token()
            response = requests.get(self.api_url+endpoint, headers={"Accept": "application/json", "Content-Type": "application/json",
                                                                    "Authorization": "Bearer " + self.token})
        return response

    def put_request(self, endpoint):
        response = requests.put(self.api_url+endpoint, headers={"Accept": "application/json", "Content-Type": "application/json",
                                                                "Authorization": "Bearer " + self.token})
        status_code = response.status_code
        if status_code == 401:
            self.request_new_token()
            requests.put(self.api_url+endpoint, headers={"Accept": "application/json", "Content-Type": "application/json",
                                                         "Authorization": "Bearer " + self.token})

    def get_current_playing(self):
        ENDPOINT = "/v1/me/player/currently-playing?market=DE"
        response = self.get_request(ENDPOINT)
        return response.json()

    def get_device_id(self, device_name):
        ENDPOINT = "/v1/me/player/devices"
        response = self.get_request(ENDPOINT)
        response = response.json()
        for device in response['devices']:
            if device['name'] == device_name:
                self.deviceID = device['id']

    def get_playlist(self, playlist_type):
        ENDPOINT = "/v1/search?q=%s&type=playlist&market=DE" % playlist_type
        response = self.get_request(ENDPOINT)
        response = response.json()
        list_of_playlists = []
        for playlist in response['playlists']['items']:
            playlist_dict = {
                "name": playlist['name'],
                "id": playlist['id'],
                "author": playlist['owner']['display_name'],
                "uri": playlist['uri'],
                "image_url": playlist['images'][0]['url']
            }
            list_of_playlists.append(playlist_dict)
        return list_of_playlists

    def start_playback(self, playlist_uri):
        if self.deviceID:
            ENDPOINT = "/v1/me/player/play?device_id=%s" % self.deviceID
            data = {"context_uri": playlist_uri}

            response = requests.put(self.api_url+ENDPOINT, data=json.dumps(data), headers={
                                    "Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + self.token})

            status_code = response.status_code
            if status_code == 401:
                self.request_new_token()
                response = requests.put(self.api_url+ENDPOINT, data=data, headers={
                                        "Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + self.token})
        else:
            print("Error no DeviceID")

    def pause_playback(self):
        if self.deviceID:
            ENDPOINT = "/v1/me/player/pause?device_id=%s" % self.deviceID
            self.put_request(ENDPOINT)
        else:
            print("Error no DeviceID")
