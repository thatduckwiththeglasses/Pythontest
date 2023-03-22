#El basico programa de Hello World
from unicodedata import name

#Print() imprime en pantalla, eso es todo
print("Hello World")

#input(), deja que el usuario ingrese un string
name = input('Ingrese su nombre: ')

#Type() imprime de que tipo es el dato, no olvidar "print()" para mostralo en pantalla
print(type("Hello World"))

# + se usa para agregar caracteres al string o para sumar numeros
print(12 + 5)
print('Bye ' + 'World')

#Definicion de variables, se puede con cualquier tipo de dato
name = 100
print(name)
print(type(name))

x, book = 120, 'Luna de Pluton'
print(x, book)
print(type(x),type(book))

#Convenciones, 
book_name = 'Luna de Pluton' #Snake Case
bookName = 'DG' #Camel Case
BookName = 'hola' #Pascal Case

#Constantes, los nombres claves son en mayuscula, siempre
PI = 3.14

#dir(), muestra lo que se puede hacer con el tipo de variable
frase = 'hola'
#print(dir(frase))

#Eliminar
del frase