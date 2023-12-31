from api import RickAndMortyAPI, ManyCharactersException
from character import Character

api = RickAndMortyAPI()
character_data = api.get_character(1)
characters = api.get_characters()

obj_characters = []
# Recorremos todos los datos de los personajes
for character in characters:
    # Inicializamos los personajes a partir de un diccionario. Y se almacenan en una lista.
    obj_characters.append(Character(**character))
print(obj_characters)

character_data = api.get_character(1)
character = None  # Hace que el personaje sea None para evitar traer dato erroneo o que no este definido
if character_data:
    character = Character(**character_data)
    print(character.name)

episodes = api.get_episodes()
episode_5 = api.get_episode(5)

locations = api.get_locations()
location_5 = api.get_location(5)

characters = api.get_characters()


characters_on_episode = api.get_characters_on_episode(5)

rick_sanchez = None
try:  # Intentar
    # Intentamos obtener un personaje por un nombre parcial
    # Si obtenemos solo 1 se completa la variable rick_sanchez.
    rick_sanchez = api.get_character_by_name("Rick Sanchez")
    print(f"Nombre: {rick_sanchez}")
    rick_sanchez = api.get_character_by_name("Ri")
except ManyCharactersException as error:
    # Si obtenemos más o menos de 1 personaje da error.
    # Capturamos el error y mostramos un mensaje informativo
    print(f"{error}")
else:
    # Lo vemos despues
    pass
finally:
    # Lo vemos despues
    pass


# API
# Character
# Origin
# Location

# Serie

# Instanciamos la API
# Le pedimos los datos
# Instanciamos la clase en base a los datos


import time


class TakeTime:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        print(f"elapsed time: {self.msecs} ms")


with TakeTime() as t:
    api.get_characters()
    api.get_characters()
    api.get_characters()

print("time 2")
with TakeTime() as t:
    api_1 = RickAndMortyAPI()
    api_1.characters

with TakeTime() as t:
    api_2 = RickAndMortyAPI()
    api_2.characters

    api_3 = RickAndMortyAPI()
    api_3.characters


# with TakeTime() as t:
#     api.get_episodes()
#     api.get_episodes()
#     api.get_episodes()

# with TakeTime() as t:
#     api.get_locations()
#     api.get_locations()
#     api.get_locations()
