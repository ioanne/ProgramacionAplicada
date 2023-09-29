import random


def foo(algo):
    if algo == 3:
        print("algo es 3")
        return 3
    else:
        algo = random.randint(0, 5)
        print(f"valor de algo: {algo}")
        foo(random.randint(0, 5))


foo()
