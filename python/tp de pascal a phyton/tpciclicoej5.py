#5. Hacer un programa que lea 100 Números, indique cuáles son múltiplos de 2 y contarlos.
i = 0
cont = 0
for i in range(1,9):
    num = int(input('Ingrese un numero: '))
    if num % 2 == 0:
        print(num,' es multiplo de 2')
        cont += 1
print('Cantidad de numeros multiplos de 2: ',cont)