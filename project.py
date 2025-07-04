import requests
from bs4 import BeautifulSoup
import json
<<<<<<< HEAD
import pdb
from collections import namedtuple

class WebScrapper:
    def __init__(self, objeto:str):
         self._objeto = objeto

class WebScrapperEstatico(WebScrapper):
   def __init__(self, objeto):
        super().__init__(objeto)



class WebScrapper_Dinamico(WebScrapper):
    def __init__(self, objeto):
        super().__init__(objeto)
=======

class WebScrapper:
    def __init__(self,object):
       self._object = object
>>>>>>> upstream/master

    def parsear_json(self):
       pass

    def buscar_nombre(self):
       pass

<<<<<<< HEAD
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
       except Exception as error:
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
        except Exception as error:
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
       except Exception as error:
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
       except Exception as error:
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
       except Exception as error:
          print(f"No Hay llave {error}")
    
    def crear_productos(self) -> list:
       self.products=[]
       product =namedtuple("Product", ["nombre" , "marca", "precio" , "link"])
       for i in range(len(self.names)):
         p = product(self.names[i], self.marcas[i], self.precios[i], self.links[i])
         self.products.append(p)

    def mostrar_productos(self):
       for product in self.products:
          print(product)
    


Scrapper1=PanamericanaScrapper("audifonos")
Scrapper1.parsear_json()
(Scrapper1.buscar_nombre())
Scrapper1.buscar_precio()
Scrapper1.buscar_marca()
Scrapper1.buscar_link()
Scrapper1.crear_productos()
Scrapper1.mostrar_productos()
=======
class PanamericanaScrapper(WebScrapper):
    def __init__(self,object):
        super().__init__(object)
    
    def parsear_json(self):
        url = "https://www.panamericana.com.co/audifonos-tipo-diadema-bass-13-686721/p"  
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        scripts = soup.find_all("script", type="application/ld+json")
        for script in scripts:
            
            self.data = json.loads(script.string)

        print(self.data)

    def buscar_nombre(self):
       names=[]
       keys=self.data.keys()
       for x in keys:
          if x=="name":
             names.append(self.data[x])
       return names

Web1=PanamericanaScrapper("audifonos")
Web1.parsear_json()
print(Web1.buscar_nombre())
>>>>>>> upstream/master
