#2. Calcular la suma y el producto de los números pares comprendidos entre 20 y 500.
i = 20
ac = 0
acp = 1
while i <= 500:
    ac = ac + i
    acp = acp * i
    i += 2
print('suma: ',ac)
print('productos: ',acp)