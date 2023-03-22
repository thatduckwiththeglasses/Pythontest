#7. ¿A cuánto asciende la suma de los números pares comprendidos entre 300 y 1232?
i = 300
ac = 0
while i <= 1232:
    ac = ac + i
    i += 2
print(ac)