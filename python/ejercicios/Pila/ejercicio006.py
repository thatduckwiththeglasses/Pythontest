#6. Leer una palabra y visualizarla en forma inversa

from Pila import Pila

stack = Pila()

palabra = input('Ingrese una palabra: ')

#while stack.size() < len(palabra):
    #stack.apilar()
    
for i in palabra:
    stack.apilar(i)
    
palabra_invertida = ''

while stack.size() > 0:
    palabra_invertida += stack.desapilar()
    
print(palabra_invertida)