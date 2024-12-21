while True:
    tipo_cambio = 3.8
    print("Seleccione la operación que desea realizar:")
    print("1. Convertir de Soles a Dólares")
    print("2. Convertir de Dólares a Soles")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == '1':
        soles = float(input("Ingrese la cantidad en Soles: "))
        dolares = soles * tipo_cambio
        print(f"{soles} Soles son {dolares:.2f} Dólares")
    elif opcion == '2':
        dolares = float(input("Ingrese la cantidad en Dólares: "))
        soles = dolares / tipo_cambio
        print(f"{dolares} Dólares son {soles:.2f} Soles")
    else:
        print("Opción no válida. Intente nuevamente.")

    salir = input("¿Desea realizar otra operación? (si/no): ").lower()
    if salir == 'no':
        print("Gracias por usar el Programa de Tipo de cambio!")
        break

