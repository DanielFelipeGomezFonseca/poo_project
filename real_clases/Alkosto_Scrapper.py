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
        self.__pagina = "Alkosto"

    ##! Aqui pongo las opciones del "Web Driver"
    def parsear_json(self):
        option = Options()
        option.add_argument("--headless")
        option.add_argument("--log-level=3")
        self.__driver = webdriver.Chrome(options=option)

        if self._objeto == "audifonos":
            self.__driver.get("https://www.alkosto.com/search?text=audifonos")
            time.sleep(5)

    #! Cada elemento se busca con un By. Ya sea un PATH O CLASS
    #! Uso list_C para todas las funciones, mas info per repo
    def buscar_nombre(self):
        names = self.__driver.find_elements(By.XPATH, '//h3[contains(@class, "product__item__top__title") and @data-index]')
        if not names:
            raise Exception("No se encontró ningún nombre de producto.")
        self.__names = [name.text for name in names]

    def buscar_marca(self):
        marcas = self.__driver.find_elements(By.CLASS_NAME, "product__item__information__brand")
        if not marcas:
            raise Exception("No se encontró ninguna marca.")
        self.__marcas = [marca.text for marca in marcas]

    def buscar_precio(self):
        precios = self.__driver.find_elements(By.CLASS_NAME, "price")
        if not precios:
            raise Exception("No se encontró ningún precio.")
        self.__precios = [p.text.strip() for p in precios if p.text.strip()]

    def buscar_link(self):
        links = self.__driver.find_elements(By.CLASS_NAME, "product__item__top__link")
        if not links:
            raise Exception("No se encontró ningún enlace de producto.")
        self.__links = [link.get_attribute("href") for link in links]

    def buscar_descuento(self):
        descuentos = self.__driver.find_elements(By.CLASS_NAME, "label-offer")
        if not descuentos:
            raise Exception("No se encontró ningún descuento.")
        self.__descuentos = [
            d.text.strip() if d.text.strip() else "0%" for d in descuentos
        ]

    
     ##! Se guardan los productos como una named_tuple, con distintos atributos y se guarda en self.__products
    def crear_productos(self) -> list:
        self.__products = []
        producto = namedtuple(f"{self._objeto}", ["pagina", "nombre", "marca", "precio", "descuento", "link", "disponibilidad"])
        for i in range(len(self.__names)):
            p = producto(
                self.__pagina,
                self.__names[i],
                self.__marcas[i],
                self.__precios[i],
                self.__descuentos[i],
                self.__links[i],
                "In stock"
            )
            self.__products.append(p)

    def mostrar_productos(self):
        for product in self.__products:
            print(product)
