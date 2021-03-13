import os
import pytz
import urllib
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

TOKEN = os.environ.get('BAHN_TOKEN')

class Bahn:

    def get_station_id(self, station):

        station = urllib.parse.quote(station)

        url = "https://api.deutschebahn.com/timetables/v1/station/"+station
        response = requests.get(
                url, 
                headers={"Accept": "application/xml", "Authorization": "Bearer "+TOKEN}
            )

        root = ET.fromstring(response.text)
        try:
            for station in root:
                eva = station.attrib['eva']
            return eva
        except UnboundLocalError:
            raise NameError("Station name is not valid")


    def __init__(self, station):

        self.station_id = self.get_station_id(station)


    def get_departures_for_time(self, time):
        
        day = time.strftime("%y%m%d")
        hour = time.strftime("%H")

        url = "https://api.deutschebahn.com/timetables/v1/plan/"+self.station_id+"/"+day+"/"+hour
        response = requests.get(
                url, 
                headers={"Accept": "application/xml", "Authorization": "Bearer "+TOKEN}
            )
        
        root = ET.fromstring(response.text)

        departures = []

        # GET DEPARTURES
        for departure in root:
            for info in departure:
                if info.tag in 'tl':
                    train_type = info.attrib['c']
                if info.tag in 'ar':
                    if 'l' in info.attrib:
                        train_line = info.attrib['l']
                    else:
                        train_line = ""
                if info.tag in 'dp':
                    next_stations = info.attrib['ppth'].split('|')
                    terminal_station = next_stations[len(next_stations)-1]
                    departure_time = info.attrib['pt']
                    departure_time = datetime.strptime(departure_time, '%y%m%d%H%M')
                else:
                    terminal_station = ""
                    departure_time = ""

            if terminal_station != "" and departure_time != "":
                if departure_time > time:
                    #print(train_type+train_line+" "+terminal_station)
                    #print(departure_time.strftime("%H:%M"))
                    #print()
                    dep = {
                        "time": departure_time.strftime("%H:%M"),
                        "train": train_type+train_line+" "+terminal_station
                    }
                    departures.append(dep) 
        
        return departures


    def get_next_departures(self):
        
        now = datetime.now() + timedelta(hours=1)
        now_p1 = now + timedelta(hours=1)

        next_departures = self.get_departures_for_time(now)
        next_departures = next_departures + self.get_departures_for_time(now_p1)

        next_departures = sorted(next_departures, key=lambda k: k['time'])

        return next_departures