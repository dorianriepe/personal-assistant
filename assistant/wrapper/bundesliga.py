
import requests
import json


class Bundesliga:
    def __init__(self, liga):
        if(liga == 1):
            self.liga = 'bl1'
        elif(liga == 2):
            self.liga = 'bl2'
        else:
            print('Error: No liga')

    def get_requests(self, endpoint):
        return requests.get(endpoint)

    def get_clubs(self):
        club_dicts = []
        response_clubs = self.get_requests(
            'https://www.openligadb.de/api/getavailableteams/%s/2020' % self.liga)
        if response_clubs:
            for club in response_clubs:
                club_dict = {
                    "clubID": club['TeamId'],
                    "clubName": club['TeamName'],
                    "clubShortName": club['ShortName'],
                    "teamIconUrl": club['TeamIconUrl']
                }
                club_dicts.append(club_dict)
        else:
            print('An error has occurred.')
        return club_dicts

    def get_bundesliga_results(self):
        spiele_dicts = []
        # response_spieltag = self.get_requests(
        #     'https://www.openligadb.de/api/getmatchdata/%s' % self.liga)
        response_spieltag = self.get_requests(
            'https://www.openligadb.de/api/getmatchdata/%s' % self.liga)
        #print(response_spieltag.text)
        if response_spieltag.status_code == 200:
            response_spieltag = json.loads(response_spieltag.text)
            for spiel in response_spieltag:
                spiel_dict = {
                    "liga": self.liga,
                    "spieltag": response_spieltag[0]['Group']['GroupOrderID'],
                    "matchID": spiel['MatchID'],
                    "team1ID": spiel['Team1']['TeamId'],
                    "team1ShortName": spiel['Team1']['ShortName'],
                    "team2ID": spiel['Team2']['TeamId'],
                    "team2ShortName": spiel['Team2']['ShortName']
                }

                if spiel['MatchIsFinished']:
                    spiel_dict["finished"] = True
                    spiel_dict["toreTeam1"] = spiel['MatchResults'][0]['PointsTeam1']
                    spiel_dict["toreTeam2"] = spiel['MatchResults'][0]['PointsTeam2']

                else:
                    spiel_dict["finished"] = False
                    spiel_dict["toreTeam1"] = 0
                    spiel_dict["toreTeam2"] = 0

                spiele_dicts.append(spiel_dict)
            return spiele_dicts

        else:
            print('An error has occurred.')

    def get_table_top_five(self):
        topFive = []
        response_table = self.get_requests(
            'https://www.openligadb.de/api/getbltable/%s/2020' % self.liga)
        if response_table.status_code == 200:
            response_table = json.loads(response_table.text)
            i = 1
            for rank in response_table:
                if i < 6:
                    table_entry_dict = {
                        "rank": i,
                        "clubShortName": rank['ShortName'],
                        "teamID": rank['TeamInfoId'],
                        "points": rank['Points'],
                        "teamIconUrl": rank['TeamIconUrl']
                    }
                    topFive.append(table_entry_dict)
                else:
                    break
                i += 1
            return topFive
        else:
            print('An error has occurred.')
