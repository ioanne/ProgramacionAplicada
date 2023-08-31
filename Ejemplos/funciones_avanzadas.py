def buscar_nombre(nombre, lista_nombres=None):
    print(lista_nombres)
    print(nombre)


def buscar(*args):
    for dato in args:
        print(f"Dato: {dato}")
    return args


def buscar2(**kwargs):
    for clave, valor in kwargs.items():
        print(f"La clave es: {clave}")
        print(f"El valor es: {valor}")
    return kwargs


buscar2(n1=1, n2=2, n3=3, n4=4, n5=5)


buscar(1, 2, 3, 4, 5, 6, 7, 8, 9)


buscar_nombre(nombre="Pedro", lista_nombres=["juan"])


lista = ["Juan", "Bonini", "12345678"]


def crear_persona(nombre, apellido, dni):
    pass


crear_persona(nombre=lista[0], apellido=lista[1], dni=lista[2])


def crear_persona(**kwargs):
    nombre = kwargs.get("nombre")
    apellido = kwargs.get("apellido")
    dni = kwargs.get("dni")

    if nombre and apellido and dni:
        print(f"Creando usuario {nombre} {apellido}. DNI: {dni}")
    else:
        print("No se pudo crear el usuario")


personas = [
    {"nombre": "Juan", "apellido": "Bonini", "dni": "12345678"},
    {"nombre": "Pedro", "apellido": "Picapiedra", "dni": "78678677"},
]

for persona in personas:
    crear_persona(**persona)
