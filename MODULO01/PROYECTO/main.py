import os
from time import sleep
from paquetes.lib_empresas import *

archivo = 'PROYECTO/empresas.txt'
dic_empresas= leer_archivo(archivo)

for _ in range(5):
    os.system('clear')
    opcion = menu()
    
    if opcion == 1:
         registrar(dic_empresas,archivo)
    
    elif opcion == 2:   
        mostrar(dic_empresas)

    elif opcion == 3:   
        modificar(dic_empresas,archivo)

    elif opcion == 4:   
        eliminar(dic_empresas, archivo)

    elif opcion == 5:   
        salir()
        break
    else :
        print("Opción incorrecta")  

    sleep(1)



