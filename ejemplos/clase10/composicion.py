class Habilidad:
    def __init__(self, habilidades):
        self.habilidades = habilidades

    def correr(self):
        print("Corriendo")


class Agresividad:
    def __init__(self, nivel):
        self.grado = nivel * 3 - 1

    def golpear(self):
        print("Lanzando golpe")


import abc


class Personaje(abc.ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.habilidad = Habilidad(self.habilidades)


class Orco(Personaje):
    habilidades = ["correr", "saltar"]

    def __init__(self, nombre, nivel):
        super().__init__(nombre)
        self.nivel = nivel
        self.agresividad = Agresividad(nivel=nivel)
        self.items = []


class Item:
    pass


orco = Orco("Juan")

print(orco.habilidad.correr())
print(orco.agresividad.golpear())
orco.items.append(Item(), Item())

orco.items.append(Item())
