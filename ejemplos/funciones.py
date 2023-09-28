carreras = [
    "Ingenieria en Computacion",
    "Licenciatura en Informatica",
    "Ingenieria en Informatica",
    "Ingenieria en Telematica",
    "Ingenieria en Software",
]


def buscar_carrera(carreras, nombre_carrera):
    for carrera in carreras:
        if nombre_carrera.lower() in carrera.lower():
            return carrera


print(buscar_carrera(carreras, ""))

# Scope
