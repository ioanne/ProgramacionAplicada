import time


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


start_time = time.time()
fibonacci(10)
end_time = time.time()
