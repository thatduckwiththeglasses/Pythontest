#5.Desarrollar una función que permita convertir un número romano en un número decimal

romano = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}

def romadecimal(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    elif romano[numero_romano[0]] >= romano[numero_romano[1]]:
        return romano[numero_romano[0]] + romadecimal(numero_romano[1:])
    else:
        return romadecimal(numero_romano[1:]) - romano[numero_romano[0]]
    
num = input('Ingrese el numero romano a convertir: ')

print(romadecimal(num))