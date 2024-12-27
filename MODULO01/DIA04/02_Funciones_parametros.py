def sumar_infinito(*args):
    resultado = 0
    for i, valor in enumerate(args):
        resultado += valor
        print(f"i: {i}, valor: {valor}, suma hasta el momento: {resultado}")
    return resultado

suma1 = sumar_infinito(1,2,3)
print(f"suma acumulada: {suma1}")


def calculadora(**kwargs):
    ope = kwargs.get("operacion")
    n1 = kwargs.get("n1")
    n2 = kwargs.get("n2")

    if ope == "suma":
        resultado = n1 + n2
    elif ope == "resta":
        resultado = n1 - n2
    elif ope == "multiplicar":
        resultado = n1 * n2
    elif ope == "dividir":
        resultado = n1 / n2
    else:
        resultado = 0
        print("Operación no válida")
        return
    print(f"La {ope} de {n1} y {n2} es {resultado}")
    return resultado

suma3= calculadora(operacion="suma", n1=10, n2=5)
resta3= calculadora(operacion="resta", n1=3, n2=2)
multi3= calculadora(operacion="multiplicar", n1=3, n2=2)
divi3= calculadora(operacion="dividir", n1=10, n2=2)


