import requests 

from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener el valor de la variable de entorno
TOKEN = os.getenv("TOKEN_API_PERU")  

dni = input("Ingrese el DNI: ")
api_url = "https://apiperu.dev/api/dni/"+dni

data_request = {
    "dni": dni
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(api_url, headers=headers, data=data_request)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error al consumir la API: {response.status_code}")