import mysql.connector
from prefect import task
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

@task(name="Cargar Data Neoauto")
def task_load_neoauto(autos):
    try:



        # Obtener el valor de la variable de entorno
        TOKEN = os.getenv("TOKEN_API_PERU")  
        
        
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST") ,
            user=os.getenv("DB_USER") ,
            password=os.getenv("DB_PASSWORD")  ,
            database=os.getenv("DB_NAME")   
        )
        
        cursor = conn.cursor()
        
        query_table = "CREATE TABLE IF NOT EXISTS autos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), url VARCHAR(255), precio FLOAT)"
        cursor.execute(query_table)
        
        query_insert = "INSERT INTO autos (nombre, url, precio) VALUES (%s, %s, %s)"
        
        for auto in autos:
            cursor.execute(query_insert, (auto['nombre'], auto['url'], auto['precio']))
        
        conn.commit()
        cursor.close()
        conn.close()
        print("datos guardados en bd...")
        
    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))