import csv
import json

# import 3DS.csv as games
def importGames (gameJSON):
    print("Games CSV was successfully imported.")

def listGames (gameJSON):
    print("The imported games are as listed here: ")
    for entry in gameJSON:
        print(entry['Title'])

if __name__ == "__main__":
    games = json.load(open('3DS.json','r'))
    importGames(games)
    listGames(games)
