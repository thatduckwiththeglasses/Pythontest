#Tipos de datos
#Strings, al imprimirlos en pantalla se veran igual
print("Hola")
'Hola'
'''Hola'''
print(type('Hola'))

#Numeros Enteros
print(30)
print(type(30))

#Numeros "float"
print(30.5)
print(type(30.5))

#Boolean
True
print(False)
print(type(False))

#Listas, pueden tener cualquier tipo de dato
[10, 20, 30]
['auto','avion']
print(['casa',12,True])
print(type([10,'auto']))
[]#<- Lista vacia

#Tupla, los datos no se pueden cambiar
print((10,20,55))
print(type((10,20)))
()#<- Tupla vacia

#Diccionarios, agrupa distintos tipos de datos con nombres clave
{
    "nombre": "Pepito",
    "disctancia": 120 
}
print({
    "nombre": "Pepito",
    "disctancia": 120 
})
print(type({
    "nombre": "Pepito",
    "disctancia": 120 
}))
{}#<- Diccionario vacio

#Nonetype
print(None)
print(type(None))
