from django.shortcuts import render
from .manager import FotManager
import requests
import base64

m = FotManager('https://www.fotmob.com/api')
def index(request):
    base_leagues = ['87','53','47']
    base_teams = ['8633','9825','8178']
    base_players = ['30981','1467236','1077894']
    data = {}
    data['leagues'] = []
    data['teams'] = []
    data['players'] = []
    for league in base_leagues:
        data['leagues'].append(m.getLeagueInfo('leagues',league))
    
    for team in base_teams:
        data['teams'].append(m.getTeamInfo('teams',team))
    for player in base_players:
        data['players'].append(m.get_player_info('playerData',player))
    return render(request,'soccermanager/index.html',context=data)
    
def league(request,leagueId):
    data = m.getLeagueInfo('leagues',leagueId)
    teams = []
    for teamId in data['teams']:
        info = m.getTeamInfo('teams',teamId)
        teams.append(info)
    data['teams'] = teams

    return render(request,'soccermanager/league.html',context=data)

def team(request,teamId):
    
    data = m.getTeamInfo('teams',teamId)
    return render(request,'soccermanager/team.html',context=data)

def player(request,playerId):
    data = m.get_player_info('playerData',playerId)
    try:
        headers = headers = {
    'authority': 'images.fotmob.com',
    'method': 'GET',
    'path': '/image_resources/playerimages/1467236.png',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es-419,es;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': '__gads=ID=ad9f6ca7212c5587:T=1712705220:RT=1712705220:S=ALNI_Ma_yB0WJgJ8Ntz4Yr9mmFVZQesebA; __gpi=UID=00000ddc2fd03f65:T=1712705220:RT=1712705220:S=ALNI_MaiTJTgygascXpXj6Hu-BGuaTio-A; __eoi=ID=b5c6d7de8c254655:T=1712705220:RT=1712705220:S=AA-AfjZGu1OGbD5X8Tp4_AeRaK5w; _ga=GA1.1.518270949.1712705217; _cc_id=f111e03c8e876c847f4f5dd6dda65f77; FCNEC=%5B%5B%22AKsRol9VAnRzEz89xlR76r36M4jIxbot-6wepiIwxFn9Y3S9RSlzO5A-QuT3oziNzqLU2mh32jzuPg1mh8E2k-SfrlgyiFpo4dnoeUvTcK-K97P31Gili4zxnKberMdmMa6oicqGXePkPSmZGJUzjh6TcNZk0pmNew%3D%3D%22%5D%5D; _ga_G0V1WDW9B2=GS1.1.1715005746.13.0.1715005763.0.0.0',
    'If-Modified-Since': 'Mon, 22 Apr 2024 17:23:01 GMT',
    'If-None-Match': '"ca60ab3ad388466bfc5843ed47a31626"',
    'Sec-Ch-Ua': '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
}


        res = requests.get(f'https://images.fotmob.com/image_resources/playerimages/{playerId}.png',headers=headers)
        print(res.content)
        if res.status_code == 200:
            encoded_image = base64.b64encode(res.content).decode('utf-8')
            print(encoded_image)
            data['image_data']=encoded_image
    except Exception as e:
        print(e)
    return render(request,'soccermanager/player.html',context=data)



