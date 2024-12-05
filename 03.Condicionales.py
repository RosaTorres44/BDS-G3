print("MI CALCULADORA")

#ENTRADA
numero1 = input("Ingrese nro 1 :")
numero2 = input("Ingrese nro 2 :")
operacion = input("Ingrese la opcion de la operación matemática que desea hacer (1. suma | 2.resta | 3. multiplicacion | 4. Division )")
operacion_letras=0 

#PROCESO
if (operacion == "1"): 
    resultado = int(numero1) + int(numero2)
    operacion_letras = "suma"
elif(operacion=="2"):
    resultado=int(numero1) - int(numero2)
    operacion_letras = "resta"
elif(operacion=="3"):
    resultado=int(numero1) * int(numero2)
    operacion_letras = "multiplicacion"
elif(operacion=="4"):
    resultado=int(numero1) / int(numero2)
    operacion_letras = "Division"
else : 
    print("La Operacion NO existe")
    exit()

#SALIDA
print(f"La {operacion_letras} de {numero1} y {numero2} es {resultado}")

