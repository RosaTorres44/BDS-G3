import os

ANCHO = 50 
opcion = 0 


dic_alumnos = {}


def mostrar_mensaje(mensaje):
    print('-' * ANCHO)
    print(' '* 10 + mensaje)
    print('-' * ANCHO)     

def menu():
    mostrar_mensaje("GESTION DE ALUMNOS")

    print("1. Registrar alumno")
    print("2. Mostrar alumno")
    print("3. Actualizar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

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
            print('-' * ANCHO)
            print(f"Alumno #{i}")
            print(f"DNI: {dni}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Email: {datos['email']}")
            print('-' * ANCHO)
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
