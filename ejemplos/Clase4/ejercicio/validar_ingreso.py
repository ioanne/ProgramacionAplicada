from datetime import time
import random


class ValidarAcceso:
    def __init__(self, empleado):
        self.empleado = empleado

    def en_horario_laboral(self, hora_actual: time):
        esta_en_horario_laboral = False
        if self.empleado.horario_entrada <= hora_actual <= self.empleado.horario_salida:
            esta_en_horario_laboral = True
        return esta_en_horario_laboral

    def entrada(self, hora_actual: time):
        acceso = False
        if self.en_horario_laboral(hora_actual):
            acceso = True
        return acceso

    def validar_autorizacion(self):
        autorizado = False
        # Imaginen que esto es el pedido de autorizacion al supervisor.
        if random.randint(0, 1):
            autorizado = True
        return autorizado

    def salida(self, hora_actual: time):
        acceso = False
        if self.en_horario_laboral(hora_actual):
            acceso = True
        elif self.empleado.horario_salida < hora_actual < self.empleado.entrada:
            if self.validar_autorizacion():
                acceso = True
        return acceso
