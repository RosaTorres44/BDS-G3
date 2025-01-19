import requests 

from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener el valor de la variable de entorno
TOKEN = os.getenv("TOKEN_API_PERU")  

ruc = input("Ingrese el RUC: ")
api_url = "https://apiperu.dev/api/ruc/"+ruc

data_request = {
    "ruc": ruc
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