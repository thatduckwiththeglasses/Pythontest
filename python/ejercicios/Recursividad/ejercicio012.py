#12. Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
#   números enteros.

def euclides(num,num1):
    if (num1 == 0) or (num == 0):
        return 0
    elif (num1 == 1) or (num == 1):
        return 1
    elif (num % 2 == 0) and (num1 % 2 == 0):
        return 2 * euclides(num // 2,num1 // 2)
    elif (num % 3 == 0) and (num1 % 3 == 0):
        return 3 * euclides(num // 3,num1 // 3)
    elif (num % 5 == 0) and (num1 % 5 == 0):
        return 5 * euclides(num // 5,num1 // 5)
    
print(euclides(230,550))