from lib_pokemon import PokemonApi

if __name__ == '__main__':
    pokemon_data_list = []

    api = PokemonApi()
    cantidad = input("Cuántos pokémon desea obtener?: ")
    pokemon = api.get_pokemon(cantidad)
    for poke in pokemon['results']:
        nombrePokemon = poke['name']
        urlPokemon = poke['url'] 
        
        print(f"Nombre: {nombrePokemon}")
        print(f"URL: {urlPokemon}")
        detalle = api.get_pokemondetalle(urlPokemon)
        base_experience = detalle['base_experience']
        height = detalle['height']
        weight = detalle['weight']
        front_default = detalle['sprites']['front_default'] 
        print(f"base_experience: {detalle['base_experience']}")
        print(f"height: {detalle['height']}")
        print(f"weight: {detalle['weight']}")
        sprites = detalle['sprites']
        print(f"front_default: {sprites['front_default']}") 
        print("*" * 50)
        

        
        pokemon_data = {
            'nombre': nombrePokemon,
            'base_experience': base_experience,
            'height': height,
            'weight': weight,
            'front_default': front_default
        }

        pokemon_data_list.append(pokemon_data)


    respuesta = input("¿Desea guardar los datos en la base de datos? (s/n): ")
    if respuesta.lower() == 's':
        api.insert_pokemon_to_db(pokemon_data_list)
        print("Datos guardados correctamente")
    else:
        print("Datos no guardados")
