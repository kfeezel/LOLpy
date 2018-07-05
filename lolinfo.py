# League of Legends in-game information script
# 2018
# Make any attribution to author: Kevin Feezel

#imports 
import requests
import sys
import psutil 

#asks for basic information
#try:
    #sum_name = sys.argv[1]
#except:
sum_name = 'Voyboy'
#sum_name = 'WWWWVWVWWWWWWWWW'
#region = input("What is your region?")
global api_key
api_key = "RGAPI-7657544e-3c5e-4c91-b04d-80dd0fcedf22"

#functions
#def checkforGame(summonerID):

def getSummonerID(summonerName):
    URL = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s?api_key=%s' % (summonerName, api_key)
    #print(URL)
    
    response = requests.get(URL).json()
    sum_id = response['id']

    return sum_id
    
def getPlayers(summonerID):
    URL = 'https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/%s?api_key=%s' % (summonerID, api_key)
    #print(URL)
    
    # Declare lists for storage of information
    red_team = []
    blue_team = []

    p_response = requests.get(URL).json()

    for x in p_response['participants']:
        if x['teamId'] == 100:
            blue_team.append(x['summonerName'])
        elif x['teamId'] == 200:
            red_team.append(x['summonerName'])
    
    return p_response, blue_team, red_team
    
getPlayers(getSummonerID(sum_name))

"""if 'LeagueClient.exe' in (p.name() for p in psutil.process_iter()):
    while True:
        getPlayers(getSummonerID(sum_name))
        
        
        
        print(str(blueteam),str(redteam))
        sleep(15)"""