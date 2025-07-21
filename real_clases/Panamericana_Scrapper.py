from bs4 import BeautifulSoup
from collections import namedtuple
import requests
import json
from abstract_clases.abscract_clases import WebScrapperDinamico


class PanamericanaScrapper(WebScrapperDinamico):
    #! Todos los atributos estan en privado, no se quiere q se accedan fuera de la clase
    def __init__(self, objeto: str):
        super().__init__(objeto)
        self.pagina = "Panamericana"

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

                #! En esta seccion de codigo se encuentra el BREAK, el detalle de eso esta en el github
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

    #! Uso list_C para todas las funciones, mas info per repo
    def buscar_nombre(self):
        try:
            self.names = [
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
            self.links = [
                product["item"]["@id"]
                for Json in self.data
                for product in Json["itemListElement"]
            ]
        except Exception as error:
            print(f"Hay error {error}")

    #! Se guardan los productos como una named_tuple, con distintos atributos y se guarda en self.__products
    def crear_productos(self) -> list:
        self.products = []
        producto = namedtuple(f"{self._objeto}", ["pagina", "nombre", "marca", "precio", "link", "disponibilidad"])
        for i in range(len(self.names)):
            p = producto(
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
