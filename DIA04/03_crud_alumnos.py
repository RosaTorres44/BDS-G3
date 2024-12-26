import os
from time import sleep
from matriculas.lib_alumnos import *

dic_alumnos = {
    '123456': {
        'nombre': 'Juan',
        'email': 'cesar@gmail.com' 
    },
}

while opcion < 5:
    os.system('clear')
    menu()
    opcion = int(input("Seleccione una opción: "))
    os.system('clear')
    if opcion == 1:
         registrar(dic_alumnos)
    
    elif opcion == 2:   
        mostrar(dic_alumnos)

    elif opcion == 3:   
        modificar(dic_alumnos)

    elif opcion == 4:   
        eliminar(dic_alumnos)

    elif opcion == 5:   
        salir()
    else :
        mostrar_mensaje("Opción incorrecta")  

    sleep(1)



