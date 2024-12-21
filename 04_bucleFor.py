# Programa que muestra la tabla de multiplicar de un número ingresado por teclado

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

# Mostrar la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")