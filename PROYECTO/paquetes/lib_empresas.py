import os
import sys

ANCHO = 50 
opcion = 0 

dic_empresas = {}

def mostrar_mensaje(mensaje):
    print('-' * ANCHO)
    print(' '* 10 + mensaje)
    print('-' * ANCHO)     

def menu():
    mostrar_mensaje("GESTION DE EMPRESAS")

    print("1. Registrar empresa")
    print("2. Mostrar empresa")
    print("3. Actualizar empresa")
    print("4. Eliminar empresa")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        os.system('clear')
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número.")
        opcion = 0
    return opcion


def registrar(dic_empresas, file_name):
        mostrar_mensaje("1. Registrar empresa") 

        while True:
            ruc = input("Ingrese RUC: ")
            if ruc.isdigit():
                if len(ruc) == 11:
                    break
                else:
                    print("El RUC debe contener 11 dígitos. Intente nuevamente.")
            else:
                print("El RUC debe contener solo números. Intente nuevamente.")

        razon_social = input("Ingrese razon social: ")
        direc = input("Ingrese dirección: ") 

        dic_nuevo_empresa = {
            ruc: {'razon_social': razon_social,
            'direc': direc}
        }
        dic_empresas.update(dic_nuevo_empresa)

        with open(file_name, 'a') as file:
                file.write(f"{ruc},{razon_social},{direc}\n")
        os.system('clear')
        print("Se registrò correctamente!")

        input("Presione Enter para continuar...")

        return dic_nuevo_empresa

def mostrar(dic_empresas):
        mostrar_mensaje("2. Mostrar empresa")

        for i, (ruc, datos) in enumerate(dic_empresas.items(), start=1):
            print('-' * ANCHO)
            print(f"Empresa #{i}")
            print(f"ruc: {ruc}")
            print(f"razon_social: {datos['razon_social']}")
            print(f"direc: {datos['direc']}")
            print('-' * ANCHO)
        input("Presione Enter para continuar...")


def modificar(dic_empresas, archivo):
        mostrar_mensaje("3. Actualizar empresa")

        conoce_ruc = input("¿Conoce el RUC a actualizar? (si/no): ").strip().lower()
        if conoce_ruc == 'no':
            mostrar(dic_empresas)


        ruc = input("Ingrese ruc del empresa a actualizar: ")

        if ruc in dic_empresas:

            razon_social = input("Ingrese nuevo razon_social: ")
            direc = input("Ingrese nuevo direc: ")
        

            dic_empresas[ruc]['razon_social'] = razon_social
            dic_empresas[ruc]['direc'] = direc

            with open(archivo, 'w') as file:
                for ruc, datos in dic_empresas.items():
                    file.write(f"{ruc},{datos['razon_social']},{datos['direc']}\n")
            print("Se actulizó correctamente")
            input("Presione Enter para continuar...")
        else:
            print("No existe la empresa con el RUC proporcionado")
            input("Presione Enter para continuar...")

 

        os.system('clear')

        return dic_empresas

def eliminar(dic_empresas, archivo):
        mostrar_mensaje("4. Eliminar empresa")

        conoce_ruc = input("¿Conoce el RUC a eliminar? (si/no): ").strip().lower()
        if conoce_ruc == 'no':
            mostrar(dic_empresas)

        ruc = input("Ingrese ruc del empresa a eliminar: ")

        if ruc in dic_empresas:
            dic_empresas.pop(ruc)
            print("Se eliminó correctamente")
            input("Presione Enter para continuar...")

        else:
            print("No existe la empresa con el RUC proporcionado")

        with open(archivo, 'w') as file:
            for ruc, datos in dic_empresas.items():
                file.write(f"{ruc},{datos['razon_social']},{datos['direc']}\n")

        return dic_empresas

def salir():
        mostrar_mensaje("5. Salir") 
        sys.exit()
        
#traer datos del archivo
def leer_archivo(file_name):
    file = open(file_name, 'r')
    str_empresas = file.read()
    lista_empresas = str_empresas.splitlines()
    file.close()
    for str_fila in lista_empresas:
            lista_fila = str_fila.split(',')
            dic_fila = {'razon_social': lista_fila[1], 'direc': lista_fila[2]}

            dic_nuevo_empresa = { lista_fila[0]: dic_fila } 
            dic_empresas.update(dic_nuevo_empresa)
    
    return dic_empresas
