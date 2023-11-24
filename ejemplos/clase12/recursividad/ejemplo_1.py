def cuenta_regresiva(n):
    """Siempre tienen una condición que en algun momento debe dar False.
    Se tiene que llamar a si mismo
    Tiene que tener menos de 1000 iteraciones, de lo contrario falla.
    """
    if n >= 0:
        print(n)
        resultado = n - 1
        cuenta_regresiva(resultado)


cuenta_regresiva(10)
