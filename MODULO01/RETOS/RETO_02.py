
import os
from time import sleep

#se agrega una empresa por default para poder probar el programa
dic_empresas = {
    '10829972246': {
        'razon_social': 'Empresa',
        'direccion': 'Jr Lima 123 - Lima' 
    },
}

ANCHO = 50
opcion = 0 

while opcion < 5:
    os.system('clear') #limpia la pantalla
    print('-' * ANCHO)
    print(' '* 10 + "GESTION DE EMPRESAS")
    print('-' * ANCHO)

    print("1. Registrar empresa")
    print("2. Mostrar empresa")
    print("3. Actualizar empresa")
    print("4. Eliminar empresa")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))
    os.system('clear')
    if opcion == 1:
        print('-' * ANCHO)
        print(' '* 10 + "1. Registrar empresa")
        print('-' * ANCHO)    

        ruc = input("Ingrese RUC: ")
        if len(ruc) != 11 or not ruc.isdigit():
            print("El RUC debe tener 11 dígitos y solo contener números.")
            input("Presione Enter para continuar...")
            continue
        razon_social = input("Ingrese Razon Social: ")
        direccion = input("Ingrese Direccion: ") 

        dic_nueva_empresa = {
            ruc: {'razon_social': razon_social,
            'direccion': direccion}
        }

        dic_empresas.update(dic_nueva_empresa)
    
    elif opcion == 2:   
        print('-' * ANCHO)
        print(' '* 10 + "2. Mostrar empresa")
        print('-' * ANCHO)  

        for i, (ruc, datos) in enumerate(dic_empresas.items(), start=1):
            print('-' * ANCHO)
            print(f"Empresa #{i}")
            print(f"RUC: {ruc}")
            print(f"Razon Social: {datos['razon_social']}")
            print(f"Direccion: {datos['direccion']}")
            print('-' * ANCHO)
        input("Presione Enter para continuar...")
    elif opcion == 3:   
        print('-' * ANCHO)
        print(' '* 10 + "3. Actualizar empresa")
        print('-' * ANCHO)  

        ruc = input("Ingrese RUC de la empresa a actualizar: ")
        razon_social = input("Ingrese nueva Razon Social: ")
        direccion = input("Ingrese nueva Direccion: ")

        dic_empresas[ruc]['razon_social'] = razon_social
        dic_empresas[ruc]['direccion'] = direccion

        input("Se registró correctamente, Presione Enter para continuar...")

    elif opcion == 4:   
        print('-' * ANCHO)
        print(' '* 10 + "4. Eliminar empresa")
        print('-' * ANCHO)  

        ruc = input("Ingrese RUC de la empresa a eliminar: ")
        dic_empresas.pop(ruc)

        input("Se eliminó correctamente, Presione Enter para continuar...")

    elif opcion == 5:   
        print('-' * ANCHO)
        print(' '* 10 + "5. Salir")
        print('Gracias por usar el programa')
        print('-' * ANCHO) 
    else :
        print("Opción incorrecta") 

    sleep(1) 