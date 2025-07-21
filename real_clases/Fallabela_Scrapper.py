from bs4 import BeautifulSoup
from collections import namedtuple
import requests
import json

from abstract_clases.abscract_clases import WebScrapperDinamico


class FallabelaScrapper(WebScrapperDinamico):
    #! Todos los atributos estan en privado, no se quiere q se accedan fuera de la clase
    def __init__(self, objeto: str):
        super().__init__(objeto)
        self.pagina = "Fallabela"

    #! Funcion mas importante, extrae los datos json del sitio
    def parsear_json(self) -> None: 
        self.data = []

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

                ##! En este codigo se encuentra el BREAK, el pq de esto se encuentra en el git
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

    #! Uso list_C para todas las funciones, mas info per repo
    def buscar_nombre(self):
        try:
            self.names = [
                producto["displayName"]
                for lista_productos in self.data
                for producto in lista_productos
            ]
        except Exception as error:
            print(f"Hay error {error}")
    
    def buscar_marca(self) -> list:
        try:
            self.marcas = [
                producto["topSpecifications"][0]
                if len(producto["topSpecifications"]) != 0
                else "No se encontro la marca"
                for lista_productos in self.data
                for producto in lista_productos
            ]
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_link(self) -> list:
        try:
            self.links = [
                producto["url"]
                for lista_productos in self.data
                for producto in lista_productos
            ]
        except Exception as error:
            print(f"Hay error {error}")
   
    def buscar_precio(self) -> list:
        try:
            self.precios = [
                producto["prices"][0]["price"][0]
                for lista_productos in self.data
                for producto in lista_productos
            ]
        except Exception as error:
            print(f"Hay error {error}")

    def buscar_descuento(self) -> list:
        try:
            self.descuentos = [
                producto["discountBadge"]["label"]
                if "discountBadge" in producto
                else "0"
                for lista_productos in self.data
                for producto in lista_productos
            ]
        except Exception as error:
            print(f"Hay error {error}")
   

    def crear_productos(self) -> list:
        ##! Se guardan los productos como una named_tuple, con distintos atributos y se guarda en self.__products
        self.products = []
        producto = namedtuple(f"{self._objeto}", ["pagina", "nombre", "marca", "precio", "descuento", "link", "disponibilidad"])
        for i in range(len(self.names)):
            p = producto(
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
