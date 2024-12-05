# Definir la tasa de cambio  
tasa_cambio = 3.85  # 1 dólar = 3.85 soles 
bandera = "sí"
despedida = "Gracias por usar el programa de tipo de cambio. ¡Hasta luego!"

while bandera == "sí" :
    print("\n*** Programa de tipo de cambio ***")
    print("1. Convertir de soles a dólares")
    print("2. Convertir de dólares a soles")
    print("3. Salir")
    
    # Solicitar la opción del usuario
    opcion = input("Seleccione una opción (1, 2 o 3): ")

    if opcion == "1":
        # Convertir de soles a dólares
        soles = float(input("Ingrese la cantidad en soles: "))
        dolares = soles / tasa_cambio
        print(f"{soles:.2f} soles son equivalentes a {dolares:.2f} dólares.")

    elif opcion == "2":
        # Convertir de dólares a soles
        dolares = float(input("Ingrese la cantidad en dólares: "))
        soles = dolares * tasa_cambio
        print(f"{dolares:.2f} dólares son equivalentes a {soles:.2f} soles.")

    elif opcion == "3":
        # Salir del programa
        print(despedida)
        break

    else:
        # Opción inválida
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        continue

    # Preguntar si desea continuar con bandera 
    bandera = input("\n¿Desea realizar otra conversión? (sí/no): ").strip().lower()
    if bandera != "sí":
        print(despedida)
        break

