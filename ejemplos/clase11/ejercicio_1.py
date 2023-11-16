"""
Imagina que estás desarrollando un sistema de gestión para una biblioteca digital.
Tu tarea es diseñar un conjunto de clases orientadas a objetos que permitan organizar y manipular información sobre:
libros, autores, géneros y usuarios.
Debes crear clases para representar un 'Libro', 'Autor', 'Género' y 'Usuario'.
Además, deberás implementar herencia para diferentes tipos de usuarios, como 'Estudiante' y 'Profesor'.
Utiliza la composición para manejar relaciones entre libros, autores y géneros.
Asegúrate de que el diseño sea flexible y expansible para futuras funcionalidades de la biblioteca digital.
Describe las propiedades y métodos esenciales de cada clase y cómo se relacionan entre sí en el contexto de la biblioteca.
Aplica al menos un ejemplo de cada pilar de la programación orientada a objetos (POO).
"""

"""
Composición
Herencia
Abstracción
Polimorfismo
Encapsulación
"""


class Libro:
    """En el ejercicio 2 se encuentra la manera correcta de resolverlo."""

    def __init__(self):
        self.genero = Genero()  # Composición
        self.autor = Autor(nombre="Jorge Luis", apellido="Borges")  # Composición


class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Genero:
    pass


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self._libros_leidos = []
        self.cantidad_libros_que_me_gustaron = 0

    def nombre_completo(self):  # Esta es la abstracción
        pass

    def leer_libro(self, libro, me_gusto):  # Esto es parte del encapsulación
        """Agrega un libro a la lista de libros leidos por el usuario"""
        self.libros_leidos.append(libro)
        if me_gusto:
            self.cantidad_libros_que_me_gustaron += 1
        return True

    @property
    def libros_leidos(self):  # Esto es parte del encapsulación
        return self._libros_leidos


class Estudiante(Usuario):  # Esta es la herencia
    pass


class Profesor(Usuario):
    def __init__(self, nombre, apellido, materia):
        super().__init__(nombre, apellido)
        self.materia = materia

    def nombre_completo(self):  # Implementación de la abstracción
        return f"Prof. {self.nombre} {self.apellido}"

    def leer_libro(self, libro, me_gusto):  # Implementación del polimorfismo
        return "El profesor no lee en clase"
