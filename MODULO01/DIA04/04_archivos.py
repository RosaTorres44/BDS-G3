#escribir en un archivo
file = open('MODULO01/alumnos.txt', 'w')
file.write('100,rosa, rosa@gmail.com\n')
file.close()

#append un archivo agrega al final del archivo
file = open('MODULO01/alumnos.txt', 'a')
file.write('200,cesar, cesar@gmail.com')
file.close()

file_read = open('MODULO01/alumnos.txt', 'r')
alumnos = file_read.read()
print(alumnos)

print(type(alumnos))
file_read.close()