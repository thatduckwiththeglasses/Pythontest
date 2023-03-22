#10. Obtener un algoritmo que permita calcular la siguiente serie: h(n)=1 + 1⁄2 + 1/3 + ... + 1/n

res = 1.0
i = 1
n = int(input('Ingrese un numero para el limite de la serie: '))
while i <= n:
    res = res + (1 / i)
    i += 1
print('el resultado de la serie es: ',res)