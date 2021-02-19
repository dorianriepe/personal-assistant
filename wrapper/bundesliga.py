
import requests
import json

class Bundesliga:
    
    @staticmethod
    def get_bundesliga_ergebnisse():
        # response = requests.get('https://www.openligadb.de/api/getmatchdata/bl1')
        response = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/2020/21')
        if response:
            spieltag = response.json()

            spieltagNr = spieltag[0]['Group']['GroupName']
            print("Die Ergebnisse des", spieltagNr, "Speiltags")

            for spiel in spieltag:
                matchID = spiel['MatchID']
                team1 = spiel['Team1']['ShortName']
                team2 = spiel['Team2']['ShortName']

                if spiel['MatchIsFinished']:
                    toreTeam1 = spiel['MatchResults'][0]['PointsTeam1']
                    toreTeam2 = spiel['MatchResults'][0]['PointsTeam2']

                    print( matchID, team1, ":", team2, toreTeam1, toreTeam2)

                else:
                    print (matchID, team1, ":", team2, "noch nicht entschieden!!")

        else:
            print('An error has occurred.')
    