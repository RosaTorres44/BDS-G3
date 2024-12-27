import os
from time import sleep
from lib_alumnos import *


dic_alumnos= leer_archivo('MODULO02/DIA05/alumnos.txt')

while opcion < 5:
    os.system('clear')
    opcion = menu()
    
    if opcion == 1:
         registrar(dic_alumnos,'MODULO01/alumnos.txt')
    
    elif opcion == 2:   
        mostrar(dic_alumnos)

    elif opcion == 3:   
        modificar(dic_alumnos)

    elif opcion == 4:   
        eliminar(dic_alumnos)

    elif opcion == 5:   
        salir()
    else :
        print("Opción incorrecta")  

    sleep(1)



