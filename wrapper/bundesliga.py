
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

    def get_clubs(self):
        club_dicts = []
        response_clubs = requests.get(
            'https://www.openligadb.de/api/getavailableteams/%s/2020' % self.liga)
        if response_clubs:
            json_clubs = response_clubs.json()
            for club in json_clubs:
                club_dict = {
                    "clubID": club['TeamId'],
                    "clubName": club['TeamName'],
                    "clubShortName": club['ShortName'],
                    "teamIconUrl": club['TeamIconUrl']
                }
                club_dicts.append(club_dict)

            return club_dicts
        else:
            print('An error has occurred.')

    def set_myclub(self, clubID):
        self.clubID = clubID

    def get_bundesliga_results(self):
        spiele_dicts = []
        # response_spieltag = requests.get(
        #     'https://www.openligadb.de/api/getmatchdata/%s' % self.liga)
        response_spieltag = requests.get(
            'https://www.openligadb.de/api/getmatchdata/%s/2020/21' % self.liga)

        if response_spieltag:
            json_spieltag = response_spieltag.json()

            for spiel in json_spieltag:
                spiel_dict = {
                    "liga": self.liga,
                    "spieltag": json_spieltag[0]['Group']['GroupOrderID'],
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
        response_table = requests.get(
            'https://www.openligadb.de/api/getbltable/%s/2020' % self.liga)
        if response_table:
            json_table = response_table.json()
            i = 1
            for rank in json_table:
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

    def get_myclub_results(self):
        if self.clubID:
            # response_matchday = requests.get(
            #     'https://www.openligadb.de/api/getmatchdata/%s' % self.liga)
            response_matchday = requests.get(
                'https://www.openligadb.de/api/getmatchdata/%s/2020/21' % self.liga)

            if response_matchday:
                json_matchday = response_matchday.json()

                for spiel in json_matchday:
                    if spiel['Team1']['TeamId'] == self.clubID or spiel['Team2']['TeamId'] == self.clubID:
                        spiel_dict = {
                            "liga": self.liga,
                            "matchday": json_matchday[0]['Group']['GroupOrderID'],
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

                return spiel_dict

            else:
                print('An error has occurred.')

        else:
            print('Error: no club was chosen')
