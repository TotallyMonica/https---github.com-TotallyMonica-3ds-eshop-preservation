import json

# import 3DS.csv as games
def importGames (gameJSON):
    print("Games CSV was successfully imported.")

def listGames (gameJSON):
    print("The imported games are as listed here: ")
    for entry in gameJSON:
        print(entry['Title'])

def regionGameCount (gameJSON):
    NA = 0
    JPN = 0
    PAL = 0
    Asia = 0
    errors = 0

    for entry in gameJSON:
        try:
            if not entry['Release date Japan'] == 'Unreleased':
                JPN = JPN + 1
            if not entry['Release date NA'] == 'Unreleased':
                NA = NA + 1
            if not entry['Release date Europe'] == 'Unreleased':
                PAL = PAL + 1
            if not entry['Release date Australasia'] == 'Unreleased':
                Asia = Asia + 1
        except:
            errors = errors + 1
    
    print(f"Japan has {JPN} games, North America has {NA} games, Europe has {PAL} games, and Australia/Asia has {Asia} games")
    print(f"{errors} error(s) were caught and dismissed while running")

def gamesInRegion (gameJSON):
    JPN = []
    NA = []
    PAL = []
    Asia = []
    errors = []

    i = 0


    for entry in gameJSON:
        try:
            if not entry['Release date Japan'] == 'Unreleased':
                JPN.append(i)
            if not entry['Release date NA'] == 'Unreleased':
                NA.append(i)
            if not entry['Release date Europe'] == 'Unreleased':
                PAL.append(i)
            if not entry['Release date Australasia'] == 'Unreleased':
                Asia.append(i)
        except:
            errors.append(i)

        i = i + 1

    print("Japan has the following games:")
    for entry in JPN:
        print(gameJSON[entry]['Title'])
    print("North America has the following games:")
    for entry in NA:
        print(gameJSON[entry]['Title'])
    print("Europe has the following games:")
    for entry in PAL:
        print(gameJSON[entry]['Title'])
    print("Asia/Australia has the following games:")
    for entry in Asia:
        print(gameJSON[entry]['Title'])

if __name__ == "__main__":
    games = json.load(open('3DS.json','r'))
    importGames(games)
    listGames(games)
    regionGameCount(games)
    gamesInRegion(games)
