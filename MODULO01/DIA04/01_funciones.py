def sumar(n1, n2):
    resultado = int(n1) + int(n2)
    return resultado


def sumar_con_mensaje(n1, n2):
    resultado = sumar(n1,n2)
    print(f'La suma de {n1} y {n2} es: {resultado}')
    return resultado


n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")

sumar_con_mensaje(n1, n2)

