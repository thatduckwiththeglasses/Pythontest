#8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
#   ma binario.

def binarior(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num % 2 == 0:
        return binarior(num // 2) + "0" 
    elif num % 2 == 1:
        return binarior(num // 2) + "1"

n = int(input())
print(binarior(n))