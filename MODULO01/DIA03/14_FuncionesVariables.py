#parametros args y kwargs

def suma(*args):
    """
    Suma una cantidad variable de argumentos.

    Args:
        *args: Una cantidad variable de números a sumar.

    Returns:
        int: La suma de todos los argumentos proporcionados.
    """
    resultado = 0 
    for i, valor in enumerate(args):
        resultado += valor
        print(f"i: {i}, valor: {valor}, suma hasta el momento: {resultado}") 
    return resultado

print(f"suma acumulada", suma(1,2,3,4,5,6,7,8,9,10))
