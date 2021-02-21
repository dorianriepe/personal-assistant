
import requests
import json

class Bundesliga:
    def __init__(self, club, liga):
        if(liga == 1):
            self.liga = 'bl1'
        elif(liga == 2):
            self.liga = 'bl2' 
        else:
            print('Error: No liga')
        self.club = club
    

    def get_bundesliga_ergebnisse(self):
        spiele_dicts = []
        # response = requests.get('https://www.openligadb.de/api/getmatchdata/%s' % self.liga)
        response = requests.get('https://www.openligadb.de/api/getmatchdata/%s/2020/21' % self.liga)

        if response:
            spieltag = response.json()

            for spiel in spieltag:
                spiel_dict = {
                    "liga": self.liga,
                    "spieltag": spieltag[0]['Group']['GroupOrderID'],
                    "matchID": spiel['MatchID'],
                    "team1": spiel['Team1']['ShortName'],
                    "team2": spiel['Team2']['ShortName']
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
    