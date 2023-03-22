#17. Dada una secuencia de caracteres acabada en #, mostrar los números (0..9) que en ella aparecen.

sec = []
a = input('Ingrese un caracter: ')
while a != '#':
    if  a in ['0','1','2','3','4','5','6','7','8','9']:
        sec.extend([a])
    a = input('Ingrese otro caracter: ')
print(sec) 