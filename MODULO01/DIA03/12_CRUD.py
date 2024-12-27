
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

        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ") 

        dic_nuevo_alumno = {
            dni: {'nombre': nombre,
            'email': email}
        }

        dic_alumnos.update(dic_nuevo_alumno)
    
    elif opcion == 2:   
        print('-' * ANCHO)
        print(' '* 10 + "2. Mostrar alumno")
        print('-' * ANCHO)  

        for i, (dni, datos) in enumerate(dic_alumnos.items(), start=1):
            print('-' * ANCHO)
            print(f"Alumno #{i}")
            print(f"DNI: {dni}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Email: {datos['email']}")
            print('-' * ANCHO)
        input("Presione Enter para continuar...")
    elif opcion == 3:   
        print('-' * ANCHO)
        print(' '* 10 + "3. Actualizar alumno")
        print('-' * ANCHO)  

        dni = input("Ingrese DNI del alumno a actualizar: ")
        nombre = input("Ingrese nuevo nombre: ")
        email = input("Ingrese nuevo email: ")

        dic_alumnos[dni]['nombre'] = nombre
        dic_alumnos[dni]['email'] = email

        input("Se registrò correctamente, Presione Enter para continuar...")

    elif opcion == 4:   
        print('-' * ANCHO)
        print(' '* 10 + "4. Eliminar alumno")
        print('-' * ANCHO)  

        dni = input("Ingrese DNI del alumno a eliminar: ")
        dic_alumnos.pop(dni)

        input("Se eliminò correctamente, Presione Enter para continuar...")


    elif opcion == 5:   
        print('-' * ANCHO)
        print(' '* 10 + "5. Salir")
        print('-' * ANCHO) 
    else :
        print("Opción incorrecta") 

    sleep(1)
