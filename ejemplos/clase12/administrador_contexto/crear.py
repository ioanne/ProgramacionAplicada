class MiAdministrador:
    def __init__(self):
        pass

    def __enter__(self):
        print("Entrando")
        return self

    def __exit__(self, type, value, traceback):
        print("Saliendo")


with MiAdministrador():
    print("hola mundo")


"""2.1. Hacer un administrador de contexto para notificar eventos al entrar y al
salir de un bloque de código"""

""" No se como cambiar directorios en python, pero se entiende la idea"""


class NotificarEntradaSalidaContexto:
    def __init__(self):
        pass

    def __enter__(self):
        print("Cambiando el directorio a la ruta 9")
        return self

    def __exit__(self, type, value, traceback):
        print("Volviendo al directorio original")


with NotificarEntradaSalidaContexto():
    a = 2 + 2
    print(a)
