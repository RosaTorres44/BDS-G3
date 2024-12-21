capitales = {
    'Peru': 'Lima',
    'Ecuador': 'Quito',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá'
}


while True:
    pais = input('Ingrese el nombre de un país: ').capitalize()
    if pais in capitales:
        capital = capitales.get(pais)
        print(f'La capital de {pais} es {capital}')
        eliminar_capital = input('¿Desea eliminar la capital? (si/no): ').lower()
        if eliminar_capital == 'si':
            capitales.pop(pais)
            print(f'Capital de {pais} eliminada correctamente')
        continuar = input('¿Desea continuar? (si/no): ').lower()
        if continuar != 'si':
            break
    else:
        nueva_capital = input(f'No se encuentra la capital de {pais}. Ingrese la capital: ')
        capitales[pais] = nueva_capital
        print(f'Capital de {pais} agregada correctamente.')
        print(f'La capital de {pais} es {nueva_capital}')
        continuar = input('¿Desea continuar? (si/no): ').lower()
        if continuar != 'si':
            break

    