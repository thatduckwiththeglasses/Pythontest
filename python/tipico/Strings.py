#Strings
#dir(), muestra lo que se puede hacer con el tipo de variable
frase = 'hola, bienvenido a peronia xd'
#print(dir(frase))
print(type(frase))

#var.upper, pasa todo a mayuscula
print(frase.upper())

#var.lower, pasa todo a minuscula
print(frase.lower())

#var.swapcase, cambia de minuscula a mayuscula y viseversa
print(frase.swapcase())

#var.capitalize, la primera letra de cada palabra pasa a mayuscula
print(frase.capitalize())

#var.replace, puede reemplazar una parte del string por otro
print(frase.replace('hola','adios'))

#var.count, cuenta cuantas veces se encuentra una letra en la variable
print(frase.count('o'))

#var.stratswith, define si el string empieza con cierto caracter (puede ser 1 o mas)
print(frase.startswith('h'))

#var.endswith, define si el string termina con cierto caracter (puede ser 1 o mas)
print(frase.endswith('h'))

#var.split, separa el string a partir de espacios u otros caracteres
print(frase.split()) #<- por espacios
print(frase.split('a')) #<- por caracter

#var.find, muestra en que posicion esta un caracter
print(frase.find('b'))

#len(), muestra la longitud de un string
print(len(frase))

#var.index, muestra el indice de un caracter
print(frase.index('e'))

#var.isnumeric, muestra si el string es numerico
print(frase.isnumeric())

#var.isalpha, muestra si el string es alfanumerico
print(frase.isalpha())

#formas de concatenar strings
print('La frase de hoy es: ' + frase)
print(f'La frase de hoy es: {frase}')
print('La frase de hoy es: {0}'.format(frase))