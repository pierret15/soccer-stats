import requests
class FotManager:
    def __init__(self,API_ENDPOINT):
        self.api_endpoint = API_ENDPOINT

    def get_player_info(self, API_MODIFIER, player_id):
        try:
            response = requests.get(f"{self.api_endpoint}/{API_MODIFIER}?id={player_id}")
            if response.status_code == 200:
                data = response.json()
                retrieved_data = {}
                retrieved_data['playerId'] = data['id']
                retrieved_data['name'] = data['name']
                retrieved_data['teamId'] = data['primaryTeam']['teamId']
                retrieved_data['team'] = data['primaryTeam']['teamName']
                playerstats = []
                try:
                    for info in data['playerInformation']:
                        if info['title'] == 'Country':
                            retrieved_data['country'] = info['value']['fallback'] 
                        if info['title'] == 'Market value':
                            retrieved_data['value'] = info['value']['fallback']


                except Exception as e:
                    return{"error":e}

                retrieved_data['playerstats'] = playerstats
                return retrieved_data
            else:
                print(response.status_code)
                return {'name':'Not Found'}
        except Exception as e:
            print(e)
            return {"error":e}

    def getTeamInfo(self,API_MODIFIER,team_id):
        try:
            response = requests.get(f"{self.api_endpoint}/{API_MODIFIER}?id={team_id}")
            if response.status_code == 200:
                data = response.json()
                retrieved_data = {}
                retrieved_data['teamId'] = data['details']['id']
                retrieved_data['name'] = data['details']['name']
                retrieved_data['country']=data['details']['country']
                players = []
                try:
                    for squad in data['squad']:
                        for player in squad['members']:
                            playerInfo = {}
                            if player['id'] != None:
                                playerInfo['id'] = player['id']
                            if player['role']['fallback'] != None:
                                playerInfo['role'] = player['role']['fallback']
                            if player['name'] != None:
                                playerInfo['name'] = player['name'].strip(',').strip('(').strip(')'),
                            try:
                                playerInfo['goals'] = player['goals']
                            except:
                                print(player['name'])

                            players.append(playerInfo)                   

                except Exception as e:
                    return{"error":e}
 
                retrieved_data['players'] = players
                return retrieved_data
            else:
                return {'name':'Not Found'}
        except Exception as e:
            print(e)
            return {"error":e}
                    
          
    def getLeagueInfo(self,API_MODIFIER,league_id):
        try:
            response = requests.get(f"{self.api_endpoint}/{API_MODIFIER}?id={league_id}")
            if response.status_code == 200:
                data = response.json()
                retrieved_data = {}
                retrieved_data['leagueId'] = data['details']['id']
                retrieved_data['name'] = data['details']['name']
                retrieved_data['country']=data['details']['country']
                teamsIds = []
                teamsPoints = []
                try:
                    for team in data['table'][0]['data']['table']['all']:
                        teamsIds.append(team['id'])
                    for team in data['table'][0]['data']['table']['all']:
                        teamsPoints.append(team['pts'])
                           
                except:
                    for team in data['table'][0]['data']['tables'][0]['table']['all']:
                        teamsIds.append(team['id'])
                    for team in data['table'][0]['data']['tables'][0]['table']['all']:
                        teamsPoints.append(team['pts'])
                    
                        

                retrieved_data['teams'] = teamsIds
                return retrieved_data
            else:
                print(response.status_code)
                return {'name':'Not Found'}
        except Exception as e:
            print(e)
            return {"error":e}
        


    
        
        


if __name__=='__main__':
    m = FotManager('https://www.fotmob.com/api')
    res = m.get_player_info('teams',9825)
    print(res)


