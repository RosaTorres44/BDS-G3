import requests
from bs4 import BeautifulSoup

url = 'https://neoauto.com/venta-de-autos-usados--camionetas-suv'

# Encabezados para simular un navegador
fake_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url,headers=fake_headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    autos = []
    div_autos = soup.find_all('article', class_='c-results c-results-used--premium')
    
    for autos in div_autos:
        nombre = autos.find('h2', class_='c-results__header-title').get_text(strip=True)
        link = autos.find('a', class_='c-results__link')['href']
       
        
        print(f'Nombre: {nombre}')
        print(f'URL: {link}')
        print('---')
else:
    print(f'Error {response.status_code} {response.reason}')