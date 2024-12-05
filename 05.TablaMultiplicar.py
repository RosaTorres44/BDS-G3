#Ingreso de numero
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Generar la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 13):  # Iterar del 1 al 12
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
