class Categoria:
    name = "Categoria"

    def __init__(self, nombre):
        self.nombre = nombre


class CategoriaRopa(Categoria):
    name = "CategoriaRopa"

    def __init__(self, nombre, talla):
        super().__init__(nombre)
        self.talla = talla


class CategoriaAccesorio(Categoria):
    name = "CategoriaAccesorio"

    def __init__(self, nombre, largo, material):
        super().__init__(nombre)
        self.largo = largo
        self.material = material


class CategoriaCalzado(Categoria):
    name = "CategoriaCalzado"

    def __init__(self, nombre, talle, color):
        super().__init__(nombre)
        self.talle = talle
        self.color = color
