import requests

URL = 'https://randomuser.me/api/?results=10&nat=es&noinfo'
response = requests.get(URL)

if response.status_code == 200:
    print(f"respuesta del servidor: {response.status_code}")
    data = response.json()
    for usuario in data['results']:
        print(f"Nombre: {usuario['name']['first']} {usuario['name']['last']}")
        print(f"Email: {usuario['email']}")
        print(f"Genero: {usuario}")
        print("*"*50)
        print(f"Genero: {usuario['gender']}")
else:
    print(f"Error: {response.status_code}")
    
    