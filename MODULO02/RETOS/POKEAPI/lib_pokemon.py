import requests
import mysql.connector

class PokemonApi: 
    def __init__(self, api_url = 'https://pokeapi.co/api/v2/pokemon'):
        self.api_url = api_url 
        
    def get_pokemon(self,results=1):
        URL = f'{self.api_url}?limit={results}'
        # print(URL)
        response = requests.get(URL)
        
        if response.status_code == 200:
            print("Conexión exitosa a la API")
            return response.json()            
        else:
            print(f"Error al consumir la API: {response.status_code}")
            return None
        
    def get_pokemondetalle(self,api_url):
        URL =api_url 
        response = requests.get(URL)
        if response.status_code == 200:
            print("Conexión exitosa a la API")
            return response.json()            
        else:
            print(f"Error al consumir la API: {response.status_code}")
            return None
        
    
        
    def insert_pokemon_to_db(self, pokemon_data):
        try:
            # Conexión a la base de datos
            connection = mysql.connector.connect(
                host='localhost',
                user='userbd',
                password='userbd',
                database='data3g'
            )
            cursor = connection.cursor()
            print("Conexión exitosa a la base de datos")

            # Eliminar la tabla (si existe) y crear una nueva
            cursor.execute("DROP TABLE IF EXISTS pokemon")
            connection.commit()  # Confirma los cambios después de DROP TABLE
            print("Tabla eliminada (si existía)")

            cursor.execute("""
                CREATE TABLE pokemon (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255),
                    height FLOAT,
                    weight FLOAT,
                    base_experience INT,
                    front_default VARCHAR(250)
                )
            """)
            connection.commit()  # Confirma los cambios después de CREATE TABLE
            print("Tabla creada exitosamente")

            # Insertar datos en la tabla
            for poke in pokemon_data:
                nombre = poke['nombre']
                height = poke['height']
                weight = poke['weight']
                base_experience = poke['base_experience']
                front_default = poke['front_default']

                cursor.execute("""
                    INSERT INTO pokemon (nombre, height, weight, base_experience, front_default)
                    VALUES (%s, %s, %s, %s, %s)
                """, (nombre, height, weight, base_experience, front_default))
                print(f"Guardando en la base de datos: {nombre}, {base_experience}, {height}, {weight}, {front_default}")

            # Confirmar los cambios
            connection.commit()
            print("Todos los datos se han guardado correctamente en la base de datos")

        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return False

        finally:
            # Cerrar cursor y conexión
            if cursor:
                cursor.close()
            if connection:
                connection.close()
            print("Conexión cerrada")
