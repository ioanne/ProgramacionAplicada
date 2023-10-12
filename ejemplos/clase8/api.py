import json
import requests

from character import Character


# https://rickandmortyapi.com/api/character
class API:
    URL = "https://rickandmortyapi.com/api"

    def __init__(self):
        pass

    def get_url(self, resource):
        """
        /character"""
        return f"{self.URL}{resource}"

    def _get_character(self, character_id):
        resource = f"/character/{character_id}"
        url = self.get_url(resource)
        response = requests.get(url)

        if response.ok:
            return response.json()

    def get_character(self, character_id):
        character_data = self._get_character(character_id)
        if character_data:
            return Character(**character_data)


api = API()
character = api.get_character(1)
print(character)
