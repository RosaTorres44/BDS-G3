# Programa de calculadora simple

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Solicitar al usuario que ingrese la operación deseada
operacion = input("Ingrese la operación (sumar/restar/multiplicar/dividir): ").strip().lower()

# Realizar la operación correspondiente
if operacion == "sumar":
    resultado = num1 + num2
elif operacion == "restar":
    resultado = num1 - num2
elif operacion == "multiplicar":
    resultado = num1 * num2
elif operacion == "dividir":
    resultado = num1 / num2
else:
    print("Operación no válida. Por favor, ingrese sumar , restar, multiplicar o dividir")
    exit()
print(f"El resultado de la suma es: {resultado}")
