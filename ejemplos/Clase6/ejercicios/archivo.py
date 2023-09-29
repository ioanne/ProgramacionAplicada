archivo = open("archivo.txt", "a")  # Abrimos el archivo

# Escribimos mientras el archivo este abierto
archivo.write("hola, como andan?\n")
archivo.write("escribimos una segunda linea\n")
archivo.close()

try:
    archivo.write("asd")
except:
    print("fallo")
finally:
    archivo.close()


if not archivo.closed:
    archivo.write("asd")
