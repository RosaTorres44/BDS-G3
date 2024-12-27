import os
from tabulate import tabulate

ANCHO = 50 
opcion = 0 
estilo = 'pretty'

dic_alumnos = {}


def mostrar_mensaje(mensaje):
    tabla = [[mensaje]]
    print(tabulate(tabla, tablefmt=estilo, stralign='center'))

def menu():
    mostrar_mensaje("GESTION DE ALUMNOS")
    menu_principal = [["1. Registrar alumno"],
    ["2. Mostrar alumno"],
    ["3. Actualizar alumno"],
    ["4. Eliminar alumno"],
    ["5. Salir"]]

    print(tabulate(menu_principal, tablefmt=estilo, stralign='left'))

    opcion = int(input("Seleccione una opción: "))
    os.system('clear')
    return opcion


def registrar(dic_alumnos, file_name):
        mostrar_mensaje("1. Registrar alumno") 

        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ") 

        dic_nuevo_alumno = {
            dni: {'nombre': nombre,
            'email': email}
        }
        dic_alumnos.update(dic_nuevo_alumno)

        with open(file_name, 'a') as file:
                file.write(f"{dni},{nombre},{email}\n")

        return dic_nuevo_alumno

def mostrar(dic_alumnos):
        mostrar_mensaje("2. Mostrar alumno")

        for i, (dni, datos) in enumerate(dic_alumnos.items(), start=1):
            data = []
            for dni, datos in dic_alumnos.items():
                   alumno_fila = [dni, datos['nombre'], datos['email']]
                   data.append(alumno_fila)
        print(tabulate(data, headers=['DNI', 'Nombre', 'Email'], tablefmt=estilo))
        input("Presione Enter para continuar...")


def modificar(dic_alumnos):
        mostrar_mensaje("3. Actualizar alumno")

        dni = input("Ingrese DNI del alumno a actualizar: ")
        nombre = input("Ingrese nuevo nombre: ")
        email = input("Ingrese nuevo email: ")
        
        dic_alumnos[dni]['nombre'] = nombre
        dic_alumnos[dni]['email'] = email

        input("Se registrò correctamente, Presione Enter para continuar...")

        return dic_alumnos

def eliminar(dic_alumnos):
        mostrar_mensaje("4. Eliminar alumno")
        dni = input("Ingrese DNI del alumno a eliminar: ")
        dic_alumnos.pop(dni)

        input("Se eliminò correctamente, Presione Enter para continuar...")

        return dic_alumnos

def salir():
        mostrar_mensaje("5. Salir") 
        
#traer datos del archivo
def leer_archivo(file_name):
    file = open(file_name, 'r')
    str_alumnos = file.read()
    lista_alumnos = str_alumnos.splitlines()
    file.close()
    for str_fila in lista_alumnos:
            lista_fila = str_fila.split(',')
            dic_fila = {'nombre': lista_fila[1], 'email': lista_fila[2]}

            dic_nuevo_alumno = { lista_fila[0]: dic_fila } 
            dic_alumnos.update(dic_nuevo_alumno)
    
    return dic_alumnos
