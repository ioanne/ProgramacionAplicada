# argumento : expresion


restar = lambda a, b: a - b


resultado = restar(5, 3)
print(resultado)


def restar(a, b):
    return a - b


resultado = restar(5, 3)
print(resultado)

lista1 = [5, 7]
lista2 = [3, 2]

resultados = map(restar, lista1, lista2)
print(list(resultados))


elevado_cuadrado = lambda a: a**2
resultado_elevado = map(elevado_cuadrado, [1, 3, 4, 4, 3, 3, 4, 4, 56, 5, 6])
print(list(resultado_elevado))
