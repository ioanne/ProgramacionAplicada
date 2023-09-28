""" type hints """


class Area:
    def __init__(self, nombre: str, rango_sueldo: tuple[int, int], piso: int):
        self.nombre = nombre
        self.rango_sueldo = rango_sueldo
        self.piso = piso
