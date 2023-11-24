class ExceptionPersonalized(Exception):
    pass


class ExceptionValuePersonalized(ValueError):
    pass


def foo():
    try:
        raise ExceptionPersonalized("Mensaje de error personalizado 554678")
    except ExceptionPersonalized:
        raise ExceptionValuePersonalized("Mensaje de error personalizado 1233423423")


input_value = input("Ingrese un valor: ")
if input_value == "1":
    raise ExceptionPersonalized("Mensaje de error personalizado")
elif input_value == "2":
    raise ExceptionValuePersonalized("Mensaje de error personalizado")
elif input_value == "3":
    try:
        foo()
    except ExceptionPersonalized as error:
        print("Se produjo un error:", error)

try:
    print("Acá podemos hacer algo de forma segura")
except ValueError as error:
    print("Se produjo un error:", error)
except (RuntimeError, TypeError, NameError) as error:
    print("Se produjo un error de tipo RuntimeError, TypeError o NameError", error)
except ExceptionPersonalized as error:
    print("Se produjo un error personalizado:", error)
else:
    print("Este bloque se ejecuta si no se produjo ninguna excepción")
finally:
    print("Este bloque se ejecuta siempre")
