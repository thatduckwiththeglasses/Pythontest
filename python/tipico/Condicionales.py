#Condicionales

from ast import While


x = int(input())

if x < 30:
    print(x,' es menor que 30')
elif x > 30:
    print(x,' es mayor que 30')
else:
    print(x,' es igual a 30')
    
if x > 2 and x <= 10:
     print(x,' es mayor que 2 y menor o igual que 10')
     
if (not(x == 20)):
    print(x,' no es igual a 20')
    
i = 1
while i <= x:
    print('numero ', i)
    i += 1

#for i in range(1, x):
#    print(i)