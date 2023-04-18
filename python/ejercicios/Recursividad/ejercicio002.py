# 2. Implementar una función que calcule la suma de todos los números enteros comprendidos entre 0 y un número entero positivo dado

def sumar(numero):
    """Da una suma comprendida desde 0 hasta el numero ingresado"""
    if (numero <= 0):
        return 0
    else:
        return numero + sumar(numero - 1)
    
print(sumar(2))