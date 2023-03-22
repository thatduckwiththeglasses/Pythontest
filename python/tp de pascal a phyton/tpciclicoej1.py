#1. Ingresar 5 pares de valores, en cada oportunidad emitir ambos valores y si ambos son positivos, emitir
#también su promedio.
i = 0
while i <= 5:
    num1 = int(input('ingrese numero 1: '))
    num2 = int(input('ingrese numero 2: '))
    print('los numeros son: ',num1,' y ',num2)
    if num1 > 0 and num2 > 0:
        promedio = (num1 + num2)/2
        print('El promedio es: ',promedio)
    i += 1
    