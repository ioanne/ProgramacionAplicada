class OneDivisionError(Exception):
    pass


def division(a, b):
    if b == 1:
        raise OneDivisionError("No se puede dividir por 1")
    return a / b


try:
    division(100, 1)
except OneDivisionError as err:
    print(err)


class Alarma:
    pass


class Vehiculo:
    pass


class Auto(Vehiculo):
    alarma = Alarma()


class Camioneta(Vehiculo):
    def __init__(self):
        self.alarma = Alarma()
        print(self.__class__.__name__)


Camioneta()
