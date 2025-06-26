import requests
from bs4 import BeautifulSoup

url = "https://www.ktronix.com/search?text=audifonos"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

productos = soup.find_all("div", class_="product__item-container")

print(productos)