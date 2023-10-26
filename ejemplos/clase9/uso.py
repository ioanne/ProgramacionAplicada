n1 = 8
n2 = "2"

try:
    resultado = n1 / n2
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por 0.")
except KeyError:
    print("No existe la clave")
except TypeError:
    print("No se puede dividir por un string")
except Exception:
    print("Ocurrio un error que no es ninguno de los de arriba")
else:
    print("No hubo error")
finally:
    print("Esto se ejecuta siempre")

# Buenas practicas
try:
    print("hola")
except KeyError:
    print("erro")
except ZeroDivisionError:
    print("No se puede dividir por 0.")
except TypeError:
    print("No se puede dividir por un string")
except Exception:
    print("Ocurrio un error que no es ninguno de los de arriba")
else:
    print("No hubo error")
finally:
    print("Esto se ejecuta siempre")


def foo():
    raise TypeError("Error 1")


def foo2():
    foo()


def foo3():
    foo2()


def foo4():
    foo3()


try:
    foo4()
except Exception as error:
    print(error)
    raise Exception("Error 3")

# Malas practicas
try:
    print("hola")  # Acá esta mal
    print("hola")  # Acá esta mal
    print("hola")  # Acá esta mal
except KeyError:
    print("erro")
except ZeroDivisionError:
    print("No se puede dividir por 0.")
except TypeError:
    print("No se puede dividir por un string")
except Exception:
    print("Ocurrio un error que no es ninguno de los de arriba")
else:
    print("No hubo error")
finally:
    print("Esto se ejecuta siempre")

# Malas practicas
try:
    print("hola")
except Exception:
    print("error")
