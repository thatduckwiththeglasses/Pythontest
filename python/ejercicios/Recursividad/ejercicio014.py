#14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
#   se puede convertir el número a cadena.

def sumadigit(numero):
    if numero < 10:
        return numero
    else:
        return (round(((numero / 10) - (numero // 10)) * 10)) + sumadigit(numero // 10)
    
print(sumadigit(55))