#18. Dada una secuencia de caracteres acabada en punto, obtener un algoritmo que determine cuantas
#veces aparece un determinado carácter, el cual será leído previamente.

a = input('Ingrese una frase: ')
while a.endswith('.') == False:
    a = a + input('Ingrese otro caracter: ')

busca = input('Ingrese que caracter desea buscar: ')
print(f'{busca} aparece {a.count(busca)} veces')