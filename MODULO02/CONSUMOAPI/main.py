from lib_randomuser import RandomUserApi

if __name__ == '__main__':
    api = RandomUserApi()
    results = input("Cuántos usuarios desea obtener?: ")
    usuarios = api.get_users(results)
    if usuarios:
        for usuario in usuarios['results']:
            print(f"Nombre: {usuario['name']['first']} {usuario['name']['last']}")
            print(f"Email: {usuario['email']}")
            print(f"Género: {usuario['gender']}")
            print("*" * 50)

    respuesta = input("¿Desea guardar los datos en la base de datos? (s/n): ")
    if respuesta.lower() == 's':
        api.insert_users_to_db(usuarios['results'])
        print("Datos guardados correctamente")
    else:
        print("Datos no guardados")
