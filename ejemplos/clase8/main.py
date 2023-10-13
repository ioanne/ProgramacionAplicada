from api import RickAndMortyAPI
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

# API
# Character
# Origin
# Location

# Serie

# Instanciamos la API
# Le pedimos los datos
# Instanciamos la clase en base a los datos
