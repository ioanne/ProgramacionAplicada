import threading
import time
import random


def func_1():
    num = random.randint(0, 29)
    for i in range(0, num):
        print("Hola mundo desde el thread 1")
        time.sleep(0.1)  # Simulamos entrada y salida


def func_2():
    num = random.randint(0, 10)
    for i in range(0, num):
        print("Hola mundo desde el thread 2")
        time.sleep(0.1)  # Simulando entrada y salida


thread_1 = threading.Thread(target=func_1)
thread_2 = threading.Thread(target=func_2)

print("Iniciando thread 1")
thread_1.start()
print("Thread 1 iniciado")


print("Iniciando thread 2")
thread_2.start()
print("Thread 2 iniciado")


thread_1.join()
thread_2.join()

print("Finalizo la ejecución")
