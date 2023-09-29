import time

with open("archivo.csv", "a") as archivo:
    # Siempre que estemos dentro del administrador el archivo va a estar abierto.
    archivo.write("titulo,nombre,apellido\n")
    archivo.write("pepe el pistolero,pepe,pistolin\n")
    archivo.flush()  # Escribe en el archivo
    archivo.write("pepe el pistolero,pepe,pistolin\n")
    archivo.write("pepe el pistolero,pepe,pistolin\n")

# Una vez que finaliza se cierra el archivo
