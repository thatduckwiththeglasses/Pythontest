#11. Se leen 50 pares de Números, c/u de los cuales tienen 2 valores: x e y distintos. Se pide contar en
#cuantos pares x>y y en cuantos y>x.

from random import randint


contx = 0
conty = 0
i = 0
while i <= 50:
    x = randint(1,500+1)
    y = randint(1,500+1)
    if x < y:
        conty += 1
    else:
        contx += 1
    i += 1
print('cantidad de x mayores que y: ',contx)
print('cantidad de y mayores que x: ',conty)