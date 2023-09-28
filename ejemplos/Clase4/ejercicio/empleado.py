from datetime import time

from area import Area
from validar_ingreso import ValidarAcceso


class Empleado:
    @classmethod
    def validar_sueldo(cls, sueldo):
        pass

    def __init__(
        self, nombre, horario_entrada: time, horario_salida: time, sueldo: float
    ):
        self.nombre = nombre
        self.horario_entrada = horario_entrada
        self.horario_salida = horario_salida
        self.sueldo = sueldo

        if self.validar_sueldo(sueldo):
            self.sueldo = sueldo
        else:
            raise Exception


class EmpleadoIT(Empleado):
    area = Area("Tecnología", (100000, 1000000), 15)

    @classmethod
    def validar_sueldo(cls, sueldo: float) -> bool:
        es_valido = False
        rango_desde = cls.area.rango_sueldo[0]
        rango_hasta = cls.area.rango_sueldo[1]
        if sueldo >= rango_desde and sueldo <= rango_hasta:
            es_valido = True
        return es_valido


class EmpleadoRRHH(Empleado):
    area = Area("People", (50000, 600000), 6)


entrada = time(7, 0, 0)
salida = time(20, 0, 0)
hora_actual = time(21, 0, 0)


juan = None
try:
    juan = EmpleadoIT("Juan", entrada, salida, 200000)
except Exception:
    print("El sueldo no esta dentro del rango.")
else:
    validador_acceso = ValidarAcceso(juan)
    print(validador_acceso.salida(hora_actual))

pedro = EmpleadoIT("Pedro", entrada, salida, 200000)
jose = EmpleadoRRHH("José", entrada, salida, 200000)
