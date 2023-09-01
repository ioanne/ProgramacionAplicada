from gato import Gato
from perro import Perro


perro = Perro("dylan")
gato = Gato("Turing")


# Implementamos la logica del algoritmo
print(f"El perro {perro.nombre} dice {perro.hacer_sonido()}")
print(f"El gato {gato.nombre} dice {gato.hacer_sonido()}")

perro.correr()
if perro.esta_corriendo:
    print(f"El perro {perro.nombre} esta corriendo")
else:
    print(f"El perro {perro.nombre} esta caminando")
perro.caminar()


if gato.esta_corriendo:
    print(f"El gato {gato.nombre} esta corriendo")
else:
    print(f"El gato {gato.nombre} esta caminando")
