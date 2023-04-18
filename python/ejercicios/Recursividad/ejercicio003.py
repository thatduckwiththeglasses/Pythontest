# 3.Implementar una función para calcular el producto de dos números enteros dados.

def productorec(numero1,numero2):
    """Calcula el producto de 2 numeros dados (de forma recursiva)"""
    if numero2 == 0:
        return 0
    elif numero2 >= 0:
        return numero1 + productorec(numero1,numero2 - 1)
    else:
        return -(numero1 - productorec(numero1,numero2 + 1))
print(productorec(3,-9))
        