"""
    1. Crea una clase llamada "Estudiante" con los siguientes atributos: nombre, edad y _promedio.
    Implementa tres métodos: mostrar_informacion() para mostrar los detalles del estudiante,
    actualizar_promedio(nuevo_promedio) para cambiar el promedio del estudiante y
    incrementar_edad() para aumentar en 1 la edad del estudiante cada vez que se llama.
    Además, crea una propiedad llamada promedio para acceder y modificar el promedio de
    manera controlada.
    2. Crea una clase llamada "Persona" con los atributos nombre, edad y altura. Implementa
    métodos para mostrar información, incrementar la edad y cambiar la altura.
    3. Crea una clase llamada "Perro" con los atributos nombre, raza y edad. Crea métodos para
    mostrar información, cambiar la raza y aumentar la edad.
    4. Crea una clase llamada "Cuenta" con los atributos titular, saldo y _numero_cuenta. Crea
    métodos para mostrar información, depositar y retirar dinero.
    5. Crea una clase llamada "Libro" con los atributos titulo, autor y _paginas. Implementa métodos
    para mostrar información, cambiar el autor y agregar páginas.
"""
import abc


class EstudianteAbstracto(abc.ABC):
    """Las clases abstractas, representan un contrato que debemos cumplir.
    En este caso, el contrato nos dice lo siguiente:
    La clase abstracta no se podrá instanciar.
    Los metodos mostrar_informacion, actualizar_promedio e incrementar_edad son obligatorios.

    """

    @abc.abstractmethod
    def mostrar_informacion(self):
        pass

    @abc.abstractmethod
    def actualizar_promedio(self, nuevo_promedio):
        pass

    @abc.abstractmethod
    def incrementar_edad(self, edad):
        pass


class Estudiante(EstudianteAbstracto):
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        # variable privada, es decir, no se puede acceder de forma directa.
        self._promedio = promedio
        print(self.mostrar_informacion())

    def mostrar_informacion(self):
        print(f"{self.nombre} {self.edad} {self._promedio}")

    def actualizar_promedio(self, nuevo_promedio):
        self._promedio = nuevo_promedio

    def incrementar_edad(self, edad):
        """Esta no es la mejor manera, la idea es usar variables privadas (con _ delante del nombre)"""
        self.edad = edad

    @property
    def promedio(self):
        return self._promedio


print(Estudiante(nombre="Juan", edad=31, promedio=5))

estudiante = Estudiante(nombre="Juan", edad=31, promedio=5)


class Estudiante:
    def __init__(self, promedio):
        self._promedio = promedio

    def actualizar_promedio(self, nuevo_promedio):
        self._promedio = nuevo_promedio

    @property
    def promedio(self):
        return self._promedio


# Crear un estudiante
estudiante = Estudiante("Ana", 20, 85.5)

# Obtener el promedio utilizando el getter
print(estudiante.promedio)  # Imprimirá 85.5

# Actualizar el promedio utilizando el setter personalizado
estudiante.actualizar_promedio(90.0)

# Obtener el nuevo promedio utilizando el getter
print(estudiante.promedio)  # Imprimirá 90.0
