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

    def buscar_nombre(self):
        try:
            self.names=[
                product["item"]["name"]
                for Json in self.data
                for product in Json["itemListElement"]
            ]
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_marca(self):
        try:
            self.marcas = [
        product["item"]["brand"]["name"]
        for Json in self.data
        for product in Json["itemListElement"]
    ]
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_precio(self) -> list:
        try:
            self.precios = [
                item["price"]
                for Json in self.data
                for product in Json["itemListElement"]
                for item in product["item"]["offers"]["offers"]
            ]
            
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_disponibilidad(self):
        try:
             self.disponibilidad = [
                item["availability"]
                for Json in self.data
                for product in Json["itemListElement"]
                for item in product["item"]["offers"]["offers"]
             ]
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_link(self) -> list:
             
        try:
            self.links=[
            product["item"]["@id"]
            for Json in self.data
            for product in Json["itemListElement"]
        ]
        except Exception as error:
            print(f"Hay error {error}")

    # def buscar_descripcion(self) -> list:
        #self.descripcions = []
        #try:
            #for Json in self.data:
               # d_1 = Json["itemListElement"]
                #for product in d_1:
                   # self.second_step = product["item"]
                   ## description = self.second_step["description"]
                   # self.descripcions.append(description)
       # except Exception as error:
           # print(f"Hay error {error}")

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

   def buscar_nombre(self):
      
        try:
            self.names=[
            d_1["displayName"]
            for Json in self.data
            for d_1 in Json
        ] 
        except Exception as error:
            print(f"Hay error {error}")
    
   def buscar_marca(self) -> list:
       
        try:
            self.marcas=[
            d_1["topSpecifications"][0]
            if len(d_1["topSpecifications"]) != 0
            else
            "No se encontro la marca"
            for Json in self.data
            for d_1 in Json
        ]
        except Exception as error:
            print(f"Hay error {error}")

   def buscar_link(self) -> list:
       
       try:
            self.links=[
            d_1["url"]
            for Json in self.data
            for d_1 in Json
        ] 
       except Exception as error:
            print(f"Hay error {error}")
   
   def buscar_precio(self) -> list:       
       try:
         self.precios=[
            d_1["prices"][0]["price"]
            for Json in self.data
            for d_1 in Json
        ]     
       except Exception as error:
            print(f"Hay error {error}")

   def buscar_descuento(self) -> list:
       try:
           self.descuentos=[
            d_1["discountBadge"]["label"]
            if "discountBadge" in d_1.keys()
            else
            "0"
            for Json in self.data
            for d_1 in Json 
            ]
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

Scrapper1=PanamericanaScrapper("audifonos")
Scrapper1.parsear_json()
Scrapper1.buscar_nombre()
Scrapper1.buscar_precio()
Scrapper1.buscar_marca()
Scrapper1.buscar_link()
Scrapper1.buscar_disponibilidad()
Scrapper1.crear_productos()
Scrapper1.mostrar_productos()

Scrapper2=FallabelaScrapper ("teclado")
Scrapper2.parsear_json()
Scrapper2.buscar_nombre()
Scrapper2.buscar_marca()
Scrapper2.buscar_link()
(Scrapper2.buscar_precio())
Scrapper2.buscar_descuento()
Scrapper2.crear_productos()
Scrapper2.mostrar_productos()