#10. Desarrollar un algoritmo que cuente la cantidad de digitos de un numero entero

def contar(numero):
    if numero == 0:
        return 0
    else:
        return 1 + contar(numero // 10)
    
print(contar(1225))