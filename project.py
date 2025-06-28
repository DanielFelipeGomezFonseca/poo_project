import requests
from bs4 import BeautifulSoup
import json
import pdb

class Product:
   def __init__(self, name:str):
        self.name=name

   def set_marca(self,marca):
      self.marca=marca
   

   def __str__(self):
        return f"Producto {self.name}"

class WebScrapper:
    def __init__(self, objeto:str):
         self._objeto = objeto

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
    
    def buscar_descripcion(self):
       pass

    def crear_productos(self):
       pass

    def mostrar_productos(self):
       pass

class PanamericanaScrapper(WebScrapper_Dinamico):
    def __init__(self, objeto:str):
        super().__init__(objeto)

    def parsear_json(self) -> None:
        if self._objeto== "audifonos":
            self.data=[]
            ###pdb.set_trace()
            try:
                page=1

                while True:
                  print (f"Scrapeando pagina {page}")
                  url = f"https://www.panamericana.com.co/audifonos?_q=audifonos&map=ft&page={page}"  
                  response = requests.get(url, timeout=10)
                  if response.status_code != 200:
                        raise ConnectionError("No se pudo conectar")
                  
                  soup = BeautifulSoup(response.text, "html.parser")
                  scripts = soup.find_all("script", type="application/ld+json")

                  try:
                     raw_data=json.loads(scripts[1].string)
                  except IndexError:
                     print(f"La pagina {page-1} es la ultima pagina")
                     break
                  self.data.append(raw_data)
                  page+=1

            except (requests.exceptions.Timeout , requests.exceptions.ConnectTimeout) as error: 
                print(f"Existe este {error} ")
            except (KeyboardInterrupt) as f_error:
               print(f"{f_error}")
        else: 
           raise ValueError("No existe ese scrapper aun")

    def buscar_nombre(self) ->list :
       self.names=[]
       try:
         for Json in self.data:
            d_1=Json["itemListElement"]
            for product in d_1:
             d_2=product["item"]
             name=d_2["name"]
             self.names.append(name)
       except KeyError as error:
        print(f" no  hay llave {error}")
       
    def buscar_marca(self) ->list:
        self.marcas=[]
        try:
            for Json in self.data:
               d_1=Json["itemListElement"]
               for product in d_1:
                  self.second_step=product["item"]
                  marca_inicial=self.second_step["brand"]
                  marca_final=marca_inicial["name"]
                  self.marcas.append(marca_final)
        except KeyError as error:
         print(f"No hay llave {error}")
    
    def buscar_precio(self) -> list:
       ###pdb.set_trace()
       self.precios=[]
       try:
            for Json in self.data:
               d_1=Json["itemListElement"]
               for product in d_1:
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
         for Json in self.data:
            d_1=Json["itemListElement"]
            for product in d_1:
             self.second_step=product["item"]
             link=self.second_step["@id"]
             self.links.append(link)
       except KeyError as error:
          print(f"No Hay llave {error}")
    
    def buscar_descripcion(self) ->list:
       self.descripcions=[]
       try:
         for Json in self.data:
            d_1=Json["itemListElement"]
            for product in d_1:
             self.second_step=product["item"]
             description=self.second_step["description"]
             self.descripcions.append(description)
       except KeyError as error:
          print(f"No Hay llave {error}")
    
    def crear_productos(self) -> list:
       self.products=[]
       for name in self.names:
        p=Product(name=name)
        self.products.append(p)  
       return self.products
    
    def mostrar_productos(self):
       for product in self.products:
          print(product)
    


Scrapper1=PanamericanaScrapper("audifonos")
Scrapper1.parsear_json()
(Scrapper1.buscar_nombre())
print((Scrapper1.names))
Scrapper1.buscar_precio()
print(((Scrapper1.precios)))

#Scrapper1.mostrar_productos()