#6. Dada una secuencia de caracteres, devolver la secuencia invertida

def invertir(palabra):
    if len(palabra) == 0:
        return ''
    else:
        return palabra[-1] + invertir(palabra[0:-1])
    
print(invertir('noob saibot'))