from interfaz_animal import IAnimal
from movimiento import Movimiento


class Animal(IAnimal, Movimiento):
    """En la clase animal, aplicamos la logica que queremos encapsular"""

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
