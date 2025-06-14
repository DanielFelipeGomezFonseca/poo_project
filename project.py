import requests
from bs4 import BeautifulSoup
import json


class Webscrapper():
    def __init__(self,name):
        self.name=name
    
    def buscar_json(self):
        url = "https://www.panamericana.com.co/audifonos-tipo-diadema-bass-13-686721/p"
        headers = {
        "User-Agent": "Mozilla/5.0"
            }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
         soup = BeautifulSoup(response.text, "html.parser")

         # Encuentra TODOS los bloques JSON en el HTML
        scripts = soup.find_all("script", type="application/ld+json")

        for script in scripts:
             try:
                 self.data = json.loads(script.string)
                 # Solo procesamos si es un producto
                 if self.data.get("@type") == "Product":
                    pass
             except (json.JSONDecodeError, TypeError):
              continue  # Si el bloque no es un JSON válido, lo ignoramos
        else:
            print(f"❌ Error al cargar la página. Código: {response.status_code}")


    def product_name(self):
       names=[]
       keys=self.data.keys()
       for x in keys:
          if x=="name":
             names.append(self.data[x])
       return names

Web1=Webscrapper("audifonos")
Web1.buscar_json()
print(Web1.product_name())