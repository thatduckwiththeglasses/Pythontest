#9. Implementar una función para calcular el logaritmo entero de número n en una base b. Re-
#   cuerde que: log[b](n/b)= log[b] n + log[b] b

from math import log

def logaritmo(numero,base):
    if numero == 1:
        return 0
    elif numero == base:
        return 1
    else:
        return 1 + logaritmo(numero // base,base)
    
print(log(125,5))
print(logaritmo(125,5))
print(logaritmo(125,5) + log(5,5))