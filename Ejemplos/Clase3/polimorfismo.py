class Animal:
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"


perro = Perro()
gato = Gato()

print(perro.hacer_sonido())
print(gato.hacer_sonido())
