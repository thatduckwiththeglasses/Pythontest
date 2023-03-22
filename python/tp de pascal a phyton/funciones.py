# 5!= 5 * 4 * 3 * 2 * 1 = 120
# 5!= 5 * 4!

def factorialr(numero):
    """Resuelve el Factorial de un numero dado (de manera recursiva)"""
    if numero == 0:
        return 1
    else:
        return numero * factorialr(numero - 1)

def factoriali(numero):
    """Resuelve el Factorial de un numero dado (de manera iterativa)"""
    i = 1
    factorial = 1
    while i <= numero:
        factorial = factorial * i
        i += 1
    return factorial    
print(factorialr(5))
print(factoriali(5))