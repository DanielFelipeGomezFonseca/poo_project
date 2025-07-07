import requests
from bs4 import BeautifulSoup
import json
import pdb
from collections import namedtuple


class WebScrapper:
    def __init__(self, objeto: str):
        self._objeto = objeto


class WebScrapperEstatico(WebScrapper):
    def __init__(self, objeto):
        super().__init__(objeto)


class WebScrapperDinamico(WebScrapper):
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

    def buscar_descuento(self):
        pass

    def buscar_disponibilidad(self):
        pass

    def crear_productos(self):
        pass

    def mostrar_productos(self):
        pass


class PanamericanaScrapper(WebScrapperDinamico):
    def __init__(self, objeto: str):
        super().__init__(objeto)
        self.pagina="Panamericana"

    def parsear_json(self) -> None:
        self.data = []
        if self._objeto == "audifonos":
            url = "https://www.panamericana.com.co/audifonos?_q=audifonos&map=ft&"
        elif self._objeto == "mouse":
            url = "https://www.panamericana.com.co/mouse?_q=mouse&map=ft&"
        elif self._objeto == "teclado":
            url = "https://www.panamericana.com.co/teclado?_q=teclado&map=ft&"
        try:
            page = 1
            while True:
                print(f"Scrapeando pagina {page}")
                url_modified = url + f"page={page}"
                response = requests.get(url_modified, timeout=10)
                if response.status_code != 200:
                    raise ConnectionError("No se pudo conectar")

                soup = BeautifulSoup(response.text, "lxml")
                scripts = soup.find_all("script", type="application/ld+json")

                try:
                    raw_data = json.loads(scripts[1].string)
                except IndexError:
                    print(f"La pagina {page - 1} es la ultima pagina")
                    break

                self.data.append(raw_data)
                page += 1

        except (requests.exceptions.Timeout, requests.exceptions.ConnectTimeout) as error:
            print(f"Existe este {error}")
        except KeyboardInterrupt as f_error:
            print(f"{f_error}")

    def buscar_nombre(self) -> list:
        self.names = []
        try:
            for Json in self.data:
                d_1 = Json["itemListElement"]
                for product in d_1:
                    d_2 = product["item"]
                    name = d_2["name"]
                    self.names.append(name)
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_marca(self) -> list:
        self.marcas = []
        try:
            for Json in self.data:
                d_1 = Json["itemListElement"]
                for product in d_1:
                    self.second_step = product["item"]
                    marca_inicial = self.second_step["brand"]
                    marca_final = marca_inicial["name"]
                    self.marcas.append(marca_final)
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_precio(self) -> list:
        self.precios = []
        try:
            for Json in self.data:
                d_1 = Json["itemListElement"]
                for product in d_1:
                    self.second_step = product["item"]
                    third_step = self.second_step["offers"]
                    fourth_step = third_step["offers"]
                    for item in fourth_step:
                        price = item["price"]
                    self.precios.append(price)
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_disponibilidad(self):
        self.disponibilidad = []
        try:
            for Json in self.data:
                d_1 = Json["itemListElement"]
                for product in d_1:
                    self.second_step = product["item"]
                    third_step = self.second_step["offers"]
                    fourth_step = third_step["offers"]
                    for item in fourth_step:
                        disponibilidad = item["availability"]
                        self.disponibilidad.append(disponibilidad)
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_link(self) -> list:
        self.links = []
        try:
            for Json in self.data:
                d_1 = Json["itemListElement"]
                for product in d_1:
                    self.second_step = product["item"]
                    link = self.second_step["@id"]
                    self.links.append(link)
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_descripcion(self) -> list:
        self.descripcions = []
        try:
            for Json in self.data:
                d_1 = Json["itemListElement"]
                for product in d_1:
                    self.second_step = product["item"]
                    description = self.second_step["description"]
                    self.descripcions.append(description)
        except Exception as error:
            print(f"Hay error {error}")

    def crear_productos(self) -> list:
        self.products = []
        product = namedtuple(f"{self._objeto}", ["pagina", "nombre", "marca", "precio", "link", "disponibilidad"])
        for i in range(len(self.names)):
            p = product(
                self.pagina,
                self.names[i],
                self.marcas[i],
                self.precios[i],
                self.links[i],
                self.disponibilidad[i]
            )
            self.products.append(p)

    def mostrar_productos(self):
        for product in self.products:
            print(product)

class FallabelaScrapper(WebScrapperDinamico):
   def __init__(self, objeto: str):
        super().__init__(objeto)
        self.pagina="Fallabela"

   def parsear_json(self) -> None:
        
        self.data=[]

        if self._objeto == "audifonos":
            url = "https://www.falabella.com.co/falabella-co/category/cat50670/Audifonos?sred=audifonos&"
        elif self._objeto == "mouse":
            url = "https://www.falabella.com.co/falabella-co/search?Ntt=mouse&"
        elif self._objeto == "teclado":
            url = "https://www.falabella.com.co/falabella-co/search?Ntt=teclado&"

        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            page = 1
            while True:
                print(f"Scrapeando pagina {page}")
                url_modified = url + f"page={page}"
                response = requests.get(url_modified, headers=headers, timeout=10)
                if response.status_code != 200:
                    raise ConnectionError("No se pudo conectar")
                
                soup = BeautifulSoup(response.text, "lxml")
                script = soup.find("script", attrs={"id": "__NEXT_DATA__"})
                raw_json = json.loads(script.get_text())

                try:
                    productos = raw_json["props"]["pageProps"]["results"] 
                except KeyError:             
                    print(f"La pagina {page - 1} es la ultima pagina")
                    break

                self.data.append(productos)

                page += 1
                
        except (requests.exceptions.Timeout, requests.exceptions.ConnectTimeout) as error:
            print(f"Existe este {error}")
        except KeyboardInterrupt as f_error:
            print(f"{f_error}")

   def buscar_nombre(self) -> list:
        self.names = []
        try:
            for Json in self.data:
               for d_1 in Json:
                   name=d_1["displayName"]
                   self.names.append(name)
        except Exception as error:
            print(f"Hay error {error}")
    
   def buscar_marca(self) -> list:
        self.marcas = []
        try:
            for Json in self.data:
               for d_1 in Json:
                   first_step=d_1["topSpecifications"]
                   if len(first_step) != 0:
                    d_2=first_step[0]
                    self.marcas.append(d_2)
                   else: 
                       self.marcas.append("No se encontro la marca")
        except Exception as error:
            print(f"Hay error {error}")

   def buscar_link(self) -> list:
       self.links = []
       try:
            for Json in self.data:
               for d_1 in Json:
                   link=d_1["url"]
                   self.links.append(link)
       except Exception as error:
            print(f"Hay error {error}")
   
   def buscar_precio(self) -> list:
       self.precios=[]
       try:
            for Json in self.data:
               for d_1 in Json:
                   f_1=d_1["prices"]
                   f_2=f_1[0]
                   precios=f_2.get("price","")
                   for precio in precios:
                    self.precios.append(precio)   
       except Exception as error:
            print(f"Hay error {error}")

   def buscar_descuento(self) -> list:
       self.descuentos=[]
       try:
            for Json in self.data:
               for d_1 in Json:
                   if "discountBadge" in d_1.keys():
                    f_1=d_1["discountBadge"]
                    descuento=f_1["label"]
                    self.descuentos.append(descuento) 
                   else: 
                       self.descuentos.append("0")  
       except Exception as error:
            print(f"Hay error {error}")

   def crear_productos(self) -> list:
        self.products = []
        product = namedtuple(f"{self._objeto}", ["pagina","nombre", "marca", "precio","descuento", "link","disponibilidad" ])
        for i in range(len(self.names)):
            p = product(
                self.pagina,
                self.names[i],
                self.marcas[i],
                self.precios[i],
                self.descuentos[i],
                self.links[i],
                "In stock"
                
            )
            self.products.append(p)

   def mostrar_productos(self):
        for product in self.products:
            print(product)

#Scrapper1=PanamericanaScrapper("audifonos")
##Scrapper1.parsear_json()
#Scrapper1.buscar_nombre()
#Scrapper1.buscar_precio()
#Scrapper1.buscar_marca()
#Scrapper1.buscar_link()
#Scrapper1.buscar_disponibilidad()
#Scrapper1.crear_productos()
#Scrapper1.mostrar_productos()

Scrapper2=FallabelaScrapper ("teclado")
Scrapper2.parsear_json()
Scrapper2.buscar_nombre()
Scrapper2.buscar_marca()
Scrapper2.buscar_link()
(Scrapper2.buscar_precio())
Scrapper2.buscar_descuento()
Scrapper2.crear_productos()
Scrapper2.mostrar_productos()