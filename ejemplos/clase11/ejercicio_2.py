class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Genero:
    def __init__(self, nombre):
        self.nombre = nombre


class Libro:
    def __init__(self, titulo, autor: dict, genero: dict):
        self.titulo = titulo
        self.autor = Autor(**autor)
        self.genero = Genero(**genero)


datos = {
    "titulo": "El Aleph",
    "autor": {"nombre": "Jorge Luis", "apellido": "Borges"},
    "genero": {"nombre": "Ficción"},
}

libro = Libro(**datos)
print(libro)
