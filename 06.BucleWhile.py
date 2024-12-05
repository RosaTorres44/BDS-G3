bandera = "si"
while(bandera == "si"):
    print("========CALCULADORA CON PYTHON=============")
    numero1 = int(input("Numero 1 : "))
    numero2 = int(input("Numero 2 : "))
    operacion = int(input("""INGRESE LA OPCION DESEADA : 
                          1)SUMA
                          2)RESTA
                          3)MULTIPLICAR
                          4)DIVIDIR"""))
    if(operacion==1):
        resultado = numero1 + numero2
        operacion_letras = "Suma"
    elif (operacion==2):
        resultado = numero1 - numero2
        operacion_letras = "Resta"
    else :     
        print("La operacion no existe")

    print(f"La {operacion_letras} de {numero1} y {numero2} es {resultado}")
    bandera = input("Desea continuar? ")

