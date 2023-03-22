#15. Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales para valores
#comprendidos entre a y b. (con a<b)

a = int(input('Ingrese un numero: '))
b = int(input('Ingrese otro numero: '))
i = a
if a < b:
    while i <= b:
        j = a
        while j <= b:
            print(f'{i} x {j} = {i * j}')
            j += 1
        i += 1 