#1.Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
#   número dado.

def Fibonaccir(numero):
    """Da el valor de una sucesión de Fibonacci de un numero ingresado (de forma recursiva)"""
    if (numero == 0) or (numero == 1):
        return numero
    else:
        return Fibonaccir(numero - 1) + Fibonaccir(numero - 2)

print(Fibonaccir(4))