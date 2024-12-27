dias = ['lunes', 'martes', 'miercoles']
print(dias)
print(dias[0])
print(dias[2]) 
print(dias[-1])

print(dias[1:4]) # rangos 
print(dias[:4]) # desde el principio
print(dias[:]) # todo

#agregar 
dias.append('jueves')
dias.append('viernes')
print(dias)

#eliminar 
dias.pop(3)
print(dias)

#actualizacion 
dias[1] = 'actualizado'
print(dias)

#recorrer
print('Recorrer con for')
for dia in dias:
    print(dia)