
def sumar(num1, num2):
    """
    Suma dos números y devuelve el resultado.

    Args:
        num1 (int): El primer número a sumar.
        num2 (int): El segundo número a sumar.

    Returns:
        int: La suma de num1 y num2.
    """
    suma = num1 + num2
    return suma


def sumar_con_mensaje (num1, num2):
    """
    Suma dos números y devuelve el resultado con un mensaje.

    Args:
        num1 (int): El primer número a sumar.
        num2 (int): El segundo número a sumar.

    Returns:
        str: Un mensaje que indica la suma de num1 y num2.
    """
    suma = num1 + num2
    mensaje = f"El resultado de la suma es: {suma}"
    return mensaje


# Solicitar al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = sumar(num1, num2)

print(sumar_con_mensaje(num1, num2))