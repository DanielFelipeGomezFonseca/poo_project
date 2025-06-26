import requests
from bs4 import BeautifulSoup
import json
import pdb

class Product:
   def __init__(self, name):
        self.name=name
   
   def __str__(self):
        return f"Producto {self.name}"

class WebScrapper:
    def __init__(self, objeto:str):
         self._objecto = objeto

class WebScrapper_Dinamico(WebScrapper):
    def __init__(self, objeto):
        super().__init__(objeto)

    def parsear_json(self):
       pass

    def buscar_nombre(self):
       pass

    def buscar_marca(self):
       pass

    def buscar_precio(self):
       pass

    def buscar_link(self):
       pass

    def crear_productos(self):
       pass

    def mostrar_productos(self):
       pass

class PanamericanaScrapper(WebScrapper_Dinamico):
    def __init__(self, objeto:str):
        super().__init__(objeto)

    def parsear_json(self) -> None:
        if self._objecto== "audifonos":
            try:
                url = "https://www.panamericana.com.co/audifonos?_q=audifonos&map=ft"  
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                scripts = soup.find_all("script", type="application/ld+json")
                for script in scripts:
                    self.data = json.loads(script.string)
                ##print(self.data)
            except (TimeoutError,TypeError) as error: 
                print(f"Existe este {error} ")
        else: 
           raise ValueError("No existe ese scrapper aun")

    def buscar_nombre(self) ->list :
       self.names=[]
       try:
        self.first_step=self.data["itemListElement"]
        for product in self.first_step:
           self.second_step=product["item"]
           name=self.second_step["name"]
           self.names.append(name)
       except KeyError as error:
        print(f" no  hay llave {error}")
       return self.names
       
    def buscar_marca(self) ->list:
        self.marcas=[]
        try:
            self.first_step=self.data["itemListElement"]
            for product in self.first_step:
             self.second_step=product["item"]
             marca_inicial=self.second_step["brand"]
             marca_final=marca_inicial["name"]
             self.marcas.append(marca_final)
        except KeyError as error:
         print(f"No hay llave {error}")
        return self.marcas
    
    def buscar_precio(self) -> list:
       ###pdb.set_trace()
       self.precios=[]
       try:
            self.first_step=self.data["itemListElement"]
            for product in self.first_step:
             self.second_step=product["item"]
             third_step=self.second_step["offers"]
             fourth_step=third_step["offers"]
             for item in fourth_step:
                price=item["price"]
             self.precios.append(price)
       except KeyError as error:
          print(f"No Hay llave {error}")
   
    def buscar_link(self) -> list:
       self.links=[]
       try:
            self.first_step=self.data["itemListElement"]
            for product in self.first_step:
             self.second_step=product["item"]
             link=self.second_step["@id"]
             self.links.append(link)
       except KeyError as error:
          print(f"No Hay llave {error}")
       return self.links

    def crear_productos(self) -> Product:
       self.products=[]
       for name in self.names:
        self.products.append(Product(name=name))
       return self.products
    
    def mostrar_productos(self):
       for product in self.products:
          print(product)
    


Scrapper1=PanamericanaScrapper("audifonos")
Scrapper1.parsear_json()
Scrapper1.buscar_nombre()
Scrapper1.crear_productos()
Scrapper1.mostrar_productos()