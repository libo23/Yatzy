import requests
import time
import random
import sys
import pprint


### GLOBAL VARIABLES
players = []
leaderBoard = []



### FUNCTIONS
def breakApp():
    sys.exit("Quiting app")


def loading(msec):
    animation = "|/-\\"
    idx = 0
    while(idx < (msec/100)):
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)


def throwDice():
    min = 1
    max = 6
    loading(1200)
    return random.randint(min, max)


def getPlayersApi(numPlayers):

    url = f'https://webapi.no/api/v1/randomPersons/{numPlayers}'
    response = requests.get(url)

    if response.status_code == 200:
        for p in response.json()['data']:
            players.append({
                'player_info': p,
                'game_data': {
                    'scoreBoard': {
                        'only_one': '99',
                        'only_two': '99',
                        'only_three': '99',
                        'only_four': '99',
                        'only_five': '99',
                        'only_six': '99',
                        'one_pair': '99',
                        'two_pair': '99',
                        'three_of_kind': '99',
                        'four_of_kind': '99',
                        'full_house': '99',
                        'small_straight': '99',
                        'big_straight': '99',
                        'yatzee': '99'
                    },
                    'totalScore': 0
                }
            })
    
    return response.status_code


def getPlayers(numPlayers):
    loading(300)

    response = getPlayersApi(numPlayers)

    if response == 200:

        print('spillere hentet ut for å være med i spillet:')
        for p in players:
            p = p['player_info']
            loading(1000)
            print(f"{p['firstname']} {p['lastname']}, alder: {p['age']}")
    
    else:
        print(f"feilmelding: feil ved innhenting av spillere.")
        print(f"status code: {response}")
        breakApp() 


def startingRow(players):
    
    for p in players:
        print(f"spiller {p['player_info']['firstname']} kaster terning:")
        p['game_data']['firstDice'] = throwDice()
        print(p['game_data']['firstDice'])
    
    players = sorted(players, key=lambda d: d['game_data']['firstDice'], reverse=True)
    print(" ")

    print(f"spillerene spiller etter følgene rekkefølge:") 

    for p in players:
        print(f"{p['player_info']['firstname']} {p['player_info']['lastname']}")


def holdNrfunc(roundName):

    match roundName:
        case "only_one":
            return [1]

        case "only_two":
            return [2]

        case "only_three":
            return [3]
        
        case "only_four":
            return [4]


def playRound(player):

    dices = []
    holdingDices = []
    holdNr = []
    score = 0
    playingRound = ''

    print(" ")

    for r in player['game_data']['scoreBoard']:
        if player['game_data']['scoreBoard'][r] == '99':
            playingRound = r
            holdNr = holdNrfunc(r)
            print(f"spiller {p['player_info']['firstname']} spiller runde {r}")
            break

    

    for x in range(3):

        for i in range(5 - len(holdingDices)):
            dices.append(throwDice())

        for d in dices:
            if d in holdNr:
                holdingDices.append(d)

        print(f"spiller får { dices }")
        print(f"spiller holder {holdingDices} ")
        dices = []

    for d in holdingDices:
        score = score + d

    player['game_data']['scoreBoard'][playingRound] = score

    print(f"spiller fikk: {holdingDices} i terningkast og {score } poeng")



def calculatePoints(player):

    sum = 0

    for k in player['game_data']['scoreBoard']:
        if player['game_data']['scoreBoard'][k] != '99':
            sum = sum + player['game_data']['scoreBoard'][k]
    
    return sum


def getLeaderboard(players):
    
    for p in players:
        p['game_data']['totalScore'] = calculatePoints(p)

    leaderBoard = sorted(players, key=lambda d: d['game_data']['totalScore'], reverse=True)
    
    print('Spillet er over og resultater er:')
    for p in leaderBoard:
        print(f"{p['player_info']['firstname']} - {p['game_data']['totalScore']} poeng")


### MAIN CODE

print('Velkommen til YATZY-WORLD, her skal det spilles og ha det morro.')

print('Spillet fungerer følgene:')

print('Tast inn et tall 2-4, som indikerer antall spillerer som skal være med. ')


whileStatus = True

while(whileStatus):
    input1 = input()
    try:
        if int(input1) in range(2, 5):
            whileStatus = False
        else:
            print('du skrev ikke en verdi mellom 2 og 4')
    except: 
        print('du skrev ikke en verdi mellom 2 og 4')
    

getPlayers(input1)

loading(2000)

print('Alle spillere kaster terning om hvem som starter')
startingRow(players)


for p in players:
    playRound(p)

print(" ")

for p in players:
    playRound(p)

print(" ")    
getLeaderboard(players)

