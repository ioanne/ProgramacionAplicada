class Padre:
    def __init__(self, nombre):
        self.nombre = nombre
        print(self.nombre)


class Hija(Padre):
    def __init__(self, nombre, apellido):
        super().__init__(nombre)
        self.apellido = apellido
        print(self.nombre, self.apellido)


hija = Hija("Pepe", "pepepe")
