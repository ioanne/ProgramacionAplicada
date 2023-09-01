import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"


class PerroSalvaje(Perro):
    def atacar(self):
        return "Perro atacando"


perro = Perro()
perro_salvaje = PerroSalvaje()
gato = Gato()

print(perro.hacer_sonido())
print(gato.hacer_sonido())
print(perro_salvaje.hacer_sonido())
print(perro_salvaje.atacar())
