import requests
from bs4 import BeautifulSoup
from prefect import task

URL = 'https://neoauto.com/venta-de-autos-usados--camionetas-suv'

FAKE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

@task(name="extract_neoauto")
def task_extract_neoauto():
    response = requests.get(URL, headers=FAKE_HEADERS)
    autos = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        #print (soup.prettify)
        
        div_autos = soup.find_all('article', class_='c-results c-results-used--premium')
        
        for auto in div_autos:
            nombre = auto.find('h2', class_='c-results__header-title').get_text()
            link = auto.find('a', class_='c-results__link')['href']
            precio = auto.find('div',class_='c-results-mount__price').get_text()
            autos.append({
                'nombre': nombre,
                'url': link,
                'precio': precio
            })
    else:
        print(f'Error {response.status_code} {response.reason}')
         
    return autos 

        
