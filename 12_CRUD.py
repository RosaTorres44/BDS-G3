
import os
from time import sleep


dic_alumnos = {
    '123456': {
        'nombre': 'Juan',
        'email': 'cesar@gmail.com' 
    },
}

ANCHO = 50
opcion = 0 

while opcion < 5:
    os.system('clear')
    print('-' * ANCHO)
    print(' '* 10 + "GESTION DE ALUMNOS")
    print('-' * ANCHO)

    print("1. Registrar alumno")
    print("2. Mostrar alumno")
    print("3. Actualizar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))
    os.system('clear')
    if opcion == 1:
        print('-' * ANCHO)
        print(' '* 10 + "1. Registrar alumno")
        print('-' * ANCHO)    
    
    elif opcion == 2:   
        print('-' * ANCHO)
        print(' '* 10 + "2. Mostrar alumno")
        print('-' * ANCHO)  

    elif opcion == 3:   
        print('-' * ANCHO)
        print(' '* 10 + "3. Actualizar alumno")
        print('-' * ANCHO)  

    elif opcion == 4:   
        print('-' * ANCHO)
        print(' '* 10 + "4. Eliminar alumno")
        print('-' * ANCHO)  

    elif opcion == 5:   
        print('-' * ANCHO)
        print(' '* 10 + "5. Salir")
        print('-' * ANCHO) 
    else :
        print("Opción incorrecta") 

    sleep(1)
