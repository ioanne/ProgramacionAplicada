import time


class TakeTime:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        print("entro")
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        print(f"elapsed time: {self.msecs} ms")
        print("salgo")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


with TakeTime() as t:
    fibonacci(10)
