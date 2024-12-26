import os
from time import sleep

TIPO_CAMBIO_COMPRA = 3.8
TIPO_CAMBIO_VENTA = 3.65
bandera = True

while (bandera): 
    os.system("clear")
    print("Seleccione la operación que desea realizar:")
    print("1. Convertir de Soles a Dólares")
    print("2. Convertir de Dólares a Soles")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == '1':
        os.system("clear")
        print("Convirtiendo de Soles a Dólares...")
        soles = float(input("Ingrese la cantidad en Soles: "))
        dolares = soles / TIPO_CAMBIO_COMPRA
        print(f"{soles} Soles son {dolares:.2f} Dólares")
    elif opcion == '2':
        os.system("clear")
        print("Convirtiendo de Soles a Dólares...")
        dolares = float(input("Ingrese la cantidad en Dólares: "))
        soles = dolares * TIPO_CAMBIO_VENTA
        print(f"{dolares} Dólares son {soles:.2f} Soles")
    else:
        print("Opción no válida. Intente nuevamente.")
        continue
    salir = input("¿Desea realizar otra operación? (si/no): ").lower()
    if salir == 'no':
        print("Gracias por usar el Programa de Tipo de cambio!")
        break
    sleep(1)
    os.system("clear")
