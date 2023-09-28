import abc


class IAnimal(abc.ABC):
    @abc.abstractmethod
    def hacer_sonido(self):
        pass


class Movimiento:
    def __init__(self):
        self._corriendo = False

    def correr(self):
        self._corriendo = True
        return self._corriendo

    def caminar(self):
        self._corriendo = False
        return self._corriendo

    @property
    def esta_corriendo(self):
        """Propiedad publica para saber si esta corriendo."""
        return self._corriendo


class Animal(IAnimal, Movimiento):
    """En la clase animal, aplicamos la logica que queremos encapsular"""

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"


perro = Perro("dylan")
gato = Gato("Turing")

print(f"El perro {perro.nombre} dice {perro.hacer_sonido()}")
print(f"El gato {gato.nombre} dice {gato.hacer_sonido()}")

perro.correr()
if perro.esta_corriendo:
    print(f"El perro {perro.nombre} esta corriendo")
else:
    print(f"El perro {perro.nombre} esta caminando")
perro.caminar()


if gato.esta_corriendo:
    print(f"El gato {gato.nombre} esta corriendo")
else:
    print(f"El gato {gato.nombre} esta caminando")
