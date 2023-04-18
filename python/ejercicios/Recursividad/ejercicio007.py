#7. Desarrollar un algoritmo que permita calcular la siguiente serie: 

def serie(num):
    if num == 0:
        return 1
    elif num > 0:
        return 1 / serie(num - 1)
    else:
        return 1 / serie(num + 1)
    
print(serie(6))