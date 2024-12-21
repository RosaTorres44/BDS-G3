capitales = {
    'Peru': 'Lima',
    'Ecuador': 'Quito',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá'
}

#recorrido de diccionarios por claves 
print('='*20)
for clave in capitales.keys():
    print(clave)
print('='*20) 

#recorrido de diccionarios por valores 
print('='*20)
for valor in capitales.values():
    print(valor)
print('='*20) 


#recorrido de diccionarios por clave, valor 
print('='*20)
for clave, valor in capitales.items():
    print(f'la capital de la ',valor, 'es ', clave)
print('='*20) 