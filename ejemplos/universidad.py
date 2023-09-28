class Universidad:
    def __init__(self, carreras):
        self.carreras = carreras

    def buscar_carrera(self, nombre_carrera):
        carreras_encontradas = []
        for carrera in self.carreras:
            if nombre_carrera.lower() in carrera.lower():
                carreras_encontradas.append(carrera)
        return carreras_encontradas


class IFTS(Universidad):
    def __init__(self, carreras, es_terciario):
        # Sobreescribimos el metodo, manteniento el comportamiento del padre
        super().__init__(carreras)
        self.es_terciario = es_terciario


universidad = IFTS(["Ingenieria en Computacion", "Ingenieria en Informatica"], False)

print(universidad.buscar_carrera("compu"))
print(universidad.es_terciario)
