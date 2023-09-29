import time


def medir_tiempo(funcion):
    # wrapper = envoltorio
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # Esto es un pasamanos
        resultado = funcion(*args, **kwargs)
        end_time = time.time()
        finish_time = end_time - start_time
        print(f"Tiempo de ejecución: {finish_time}")
        return resultado

    # Devuelve la función
    return wrapper


@medir_tiempo
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibonacci(10))


def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


@medir_tiempo
def foo(n):
    return fibonacci_recursivo(n)


print(foo(10))


# Machete para decorador
def nombre_decorador(funcion):
    def wrapper(*args, **kwargs):  # Wrapper significa envoltorio
        # Se hace algo antes
        resultado = funcion(*args, **kwargs)
        # Se hace algo despues

        return resultado  # Se retorna el resultado

    # Devuelve la función
    return wrapper
