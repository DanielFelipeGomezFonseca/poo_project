from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from abstract_clases.abscract_clases import WebScrapperDinamico

class AlkostoWebScrapper(WebScrapperDinamico):
    #! Todos los atributos estan en privado, no se quiere q se accedan fuera de la clase
    def __init__(self, objeto: str):
        super().__init__(objeto)
        self.pagina = "Alkosto"

    ##! Aqui pongo las opciones del "Web Driver"
    def parsear_json(self):
        option = Options()
        option.add_argument("--headless")
        option.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=option)

        if self._objeto == "audifonos":
            self.driver.get("https://www.alkosto.com/search?text=audifonos")
            time.sleep(5)

    #! Cada elemento se busca con un By. Ya sea un PATH O CLASS
    #! Uso list_C para todas las funciones, mas info per repo
    def buscar_nombre(self):
        names = self.driver.find_elements(By.XPATH, '//h3[contains(@class, "product__item__top__title") and @data-index]')
        if not names:
            raise Exception("No se encontró ningún nombre de producto.")
        self.names = [name.text for name in names]

    def buscar_marca(self):
        marcas = self.driver.find_elements(By.CLASS_NAME, "product__item__information__brand")
        if not marcas:
            raise Exception("No se encontró ninguna marca.")
        self.marcas = [marca.text for marca in marcas]

    def buscar_precio(self):
        precios = self.driver.find_elements(By.CLASS_NAME, "price")
        if not precios:
            raise Exception("No se encontró ningún precio.")
        self.precios = [p.text.strip() for p in precios if p.text.strip()]

    def buscar_link(self):
        links = self.driver.find_elements(By.CLASS_NAME, "product__item__top__link")
        if not links:
            raise Exception("No se encontró ningún enlace de producto.")
        self.links = [link.get_attribute("href") for link in links]

    def buscar_descuento(self):
        descuentos = self.driver.find_elements(By.CLASS_NAME, "label-offer")
        if not descuentos:
            raise Exception("No se encontró ningún descuento.")
        self.descuentos = [
            d.text.strip() if d.text.strip() else "0%" for d in descuentos
        ]

    
     ##! Se guardan los productos como una named_tuple, con distintos atributos y se guarda en self.__products
    def crear_productos(self) -> list:
        self.products = []
        product = namedtuple(f"{self._objeto}", ["pagina", "nombre", "marca", "precio", "descuento", "link", "disponibilidad"])

        for i in range(len(self.names)):
            precio_limpio = int(self.precios[i].replace('$', '').replace('.', ''))

            p = product(
                self.pagina,
                self.names[i],
                self.marcas[i],
                precio_limpio,
                self.descuentos[i],
                self.links[i],
                "In stock"
            )
            self.products.append(p)

    def mostrar_productos(self):
        for product in self.products:
            print(product)

    def compilar_precios(self):
        precios = []
        for product in self.products:
            precios.append(product.precio)
        return precios

    def compilar_marcas(self):
        marcas = []
        for product in self.products:
            if product.marca not in marcas:
                marcas.append(product.marca)
        return marcas