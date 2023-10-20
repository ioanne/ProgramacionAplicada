import json
import requests

from character import Character, Location


class ManyCharactersException(Exception):
    pass


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

    def _fetch(self, resource):
        response = requests.get(resource)
        if response.ok:
            return response.json()

    def _search_resource_by(self, resources, _type, _value):
        new_resource = None
        for resource in resources:
            if _value == resource.get(_type):
                new_resource = resource
                break
        return new_resource

    def _partial_search_by_name(self, resources, name):
        """Acá hay tres maneras de hacer lo mismo

        Manera 1:
            values = []
            for resource in resources:
                if name in resource.get("name"):
                    values.append(resource)
            return values

        Manera 2:
            values = [resource for resource in resources if name in resource.get("name")]
            return values

        Manera 3:
            return [resource for resource in resources if name in resource.get("name")]
        """
        return [resource for resource in resources if name in resource.get("name")]

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
        """Obtener todos los episodios de rick and morty"""
        resource = f"/episode"
        return self._fetch_all(resource)

    def get_episode(self, episode_id: str) -> dict | None:
        """Obtener un único episodio de rick and morty"""
        episodes = self.get_episodes()
        return self._search_resource_by(episodes, "id", episode_id)

    def get_locations(self) -> list | None:
        """Obtener todas las locaciones de rick and morty"""
        resource = f"/location"
        return self._fetch_all(resource)

    def get_location(self, location_id: str) -> dict | None:
        """Obtener una única locación de rick and morty"""
        locations = self.get_locations()
        return self._search_resource_by(locations, "id", location_id)

    def get_characters_by_name(self, name: str) -> list[dict] | None:
        """Obtener personajes por nombre parcial."""
        characters = self.get_characters()
        return self._partial_search_by_name(characters, name)

    def get_character_by_name(self, name: str) -> dict | None:
        """Obtener un personaje por nombre parcial. Si hay mas de 1 deben dar error. (raise)"""

        characters = self.get_characters_by_name(name)
        if len(characters) == 1:
            return characters[0]
        else:
            raise ManyCharactersException("Error hay más de 1 personaje")

    def get_episode_by_name(self, name: str):
        """Obtener un episodio por nombre parcial ('Epi' in episode). Si hay mas de 1 deben dar error. (raise)"""
        pass

    def get_characters_on_episode(self, episode_id: int):
        """Obtener todos los personajes que aparecieron en un episodio."""
        characters = []
        # Obtenemos el episodio por ID
        episode = self.get_episode(episode_id)
        # Obtenemos todas las URLS donde estan los personajes
        characters_resource = episode.get("characters")
        if characters_resource:  # Validamos que haya recursos para los personajes
            for character_resource in characters_resource:
                # Recorremos cada URL y le hacemos un get para obtener la información
                # Almacenamos los personajes en una lista.
                characters.append(self._fetch(character_resource))
        return characters
