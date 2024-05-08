import requests
class FotManager:
    def __init__(self,API_ENDPOINT):
        self.api_endpoint = API_ENDPOINT

    def get_player_info(self,API_MODIFIER,player_id):
        response = requests.get(f"{self.api_endpoint}/{API_MODIFIER}?id={player_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return {}
