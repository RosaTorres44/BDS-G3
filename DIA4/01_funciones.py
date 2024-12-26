def sumar(n1, n2):
    resultado = int(n1) + int(n2)
    return resultado


n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")

suma = sumar(n1, n2)

print(f'La suma de {n1} y {n2} es: {suma}')