#15. Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
#   Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
#   el número a calcular su raíz.

def raizcuadrada(numero):
    if (numero // 2) == 1:
        return numero
    else:
        return raizcuadrada(numero // 2)

print(raizcuadrada(9))