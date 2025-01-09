from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
       
    if books:
        book = books[0]
        title = book.find('h3').find('a')['title']
        image_url = book.find('img')['src']
        imagen_text = book.find('img').find('alt')
        print(title)
        print(f"Image URL: {image_url}")
        print(f"Imagen: {imagen_text}")


    else:
        print(f'Error: {response.status_code}')