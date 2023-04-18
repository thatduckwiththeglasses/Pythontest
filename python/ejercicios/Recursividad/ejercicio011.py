#11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

from ejercicio010 import contar

def invertir(numero):
    if numero < 10:
        return numero
    else:
        num = round(((numero / 10) - (numero // 10)) * 10)
        return (num * (10 ** (contar(numero)-1))) + invertir(numero // 10)

def invertir_revisado(numero):
    if numero // 10 == 0:
        return numero
    else:
        return ((numero % 10) * (10 ** len(str(numero // 10)))) + invertir(numero // 10)

    
print(invertir(5402)) 