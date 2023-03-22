#6. Hacer un programa que lea 8 caracteres e indique que cantidad de '*' y que cantidad de letras 'a'
#aparecen.
pala = input('Ingrese una letra o palabra: ')
while len(pala) <= 8:
    pala = pala + input('Ingrese otra letra: ')
print('cantidad de *: ',pala.count('*'))
print('cantidad de a: ',pala.count('a'))