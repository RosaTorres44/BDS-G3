import requests
import mysql.connector

class RandomUserApi: 
    def __init__(self, api_url = 'https://randomuser.me/api/'):
        self.api_url = api_url 
        
    def get_users(self,results=1):
        URL = f'{self.api_url}?results={results}'
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al consumir la API: {response.status_code}")
            return None
      
    
        
    def insert_users_to_db(self,users):
        try:
            
            connection = mysql.connector.connect(
                host='localhost',
                user='userbd',
                password='userbd',
                database='data3g'
                )     
            cursor = connection.cursor()
            print("Conexión exitosa a la base de datos")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    email VARCHAR(255),
                    gender VARCHAR(50)
                )
            """)
            print("Tabla creada exitosamente")  
            for user in users:
                nombre = user['name']['first'] 
                email = user['email']
                genero = user['gender']
                cursor.execute("""
                    INSERT INTO users (name, email, gender) VALUES (%s, %s, %s)
                """, (f"{nombre} ", email, genero))                
                print(f"Guardando en la base de datos: {nombre} , {email}, {genero}")
 
            connection.commit()
     
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return False
        
        
              
            