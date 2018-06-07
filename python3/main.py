def breakTest():
    """look where and how break and else interact"""
    for n in range(10):
        print("n=")
        print(n)
        for x in range(n):
            print("x=")
            print(x)
            if x == 2:
                print("2 gevonden")
                break
        else:
            print("2 niet gevonden")

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
