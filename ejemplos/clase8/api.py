import json
import requests

from character import Character, Episode, Location


# https://rickandmortyapi.com/api/character
class RickAndMortyAPI:
    URL = "https://rickandmortyapi.com/api"

    def __init__(self):
        pass

    def get_url(self, resource: str) -> str:
        """
        /character"""
        return f"{self.URL}{resource}"

    def _fetch_all(self, resource):
        data = []
        while True:
            url = self.get_url(resource)
            response = requests.get(url)
            if response.ok:
                response_json = response.json()
                data.extend(response_json.get("results", []))
                resource = response_json.get("info", {}).get("next")
            else:
                break
        return data

    def get_characters(self) -> list | None:
        """Obtener todos los personajes de rick and morty"""
        resource = "/character"
        return self._fetch_all(resource)

    def get_character(self, character_id: str) -> dict | None:
        """Obtener un único personaje de rick and morty"""
        resource = f"/character/{character_id}"
        url = self.get_url(resource)
        response = requests.get(url)

        if response.ok:
            return response.json()

    def get_episodes(self) -> list | None:
        """ "Obtener todos los episodios de rick and morty"""
        pass

    def get_episode(self, episode_id: str) -> dict | None:
        """Obtener un único episodio de rick and morty"""
        pass

    def get_locations(self) -> list | None:
        """Obtener todas las locaciones de rick and morty"""
        pass

    def get_location(self, location_id: str) -> dict | None:
        """Obtener una única locación de rick and morty"""
        pass

    def get_character_by_name(self, name: str) -> Character | None:
        """Obtener un personaje por nombre parcial. Si hay mas de 1 deben dar error. (raise)"""
        pass

    def get_characters_by_name(self, name: str) -> list[Character] | None:
        """Obtener un personaje por nombre parcial."""
        pass

    def get_episode_by_name(self, name: str):
        """Obtener un episodio por nombre parcial ('Epi' in episode). Si hay mas de 1 deben dar error. (raise)"""
        pass

    def get_characters_on_episode(self, name: str):
        """Obtener todos los personajes que aparecieron en un episodio."""
        pass
