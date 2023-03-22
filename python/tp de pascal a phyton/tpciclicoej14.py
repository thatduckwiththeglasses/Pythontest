#14. Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales hasta el No 10. Ej. 5 por 1 es 5 5 por 2 es 10 5 por 3 es 15 15.

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f'{i} x {j} = {i * j} ')
        j += 1
    i += 1