from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from abstract_clases.abscract_clases import WebScrapperDinamico

class AlkostoWebScrapper(WebScrapperDinamico):
    def __init__(self, objeto:str):
        super().__init__(objeto)
        self.pagina="Alkosto"
    
    def parsear_json(self):
        option= Options()
        option.add_argument("--headless")
        option.add_argument("--log-level=3")

        while True:
            self.driver = webdriver.Chrome(options=option)
            self.driver.get("https://www.alkosto.com/search?text=audifonos")
            time.sleep(5)
    
    def buscar_nombre(self):
        names = self.driver.find_elements(By.XPATH, '//h3[contains(@class, "product__item__top__title") and @data-index]')
        self.names=[
            name.text for name in names
        ]

    def buscar_marca(self):
        marcas = self.driver.find_elements(By.CLASS_NAME, "product__item__information__brand")
        self.marcas=[
            marca.text for marca in marcas
        ]

    def buscar_precio(self):
        precios= self.driver.find_elements(By.CLASS_NAME, "price")
        self.precios=[
             p.text.strip() for p in precios if p.text.strip()
        ]
        print(self.precios)
    
    def buscar_descuento(self):
        descuentos = self.driver.find_elements(By.CLASS_NAME, "label-offer")
        self.descuentos=[
            descuento.text.strip() if descuento.text.strip() else "0%" for descuento in descuentos
        ]
        print(self.descuentos)

    def crear_productos(self) -> list:
        self.products = []
        product = namedtuple(f"{self._objeto}", ["pagina", "nombre", "marca", "precio", "descuento", "disponibilidad"])
        for i in range(len(self.names)):
            p = product(
                self.pagina,
                self.names[i],
                self.marcas[i],
                self.precios[i],
                self.descuentos[i],
                "In stock"
            )
            self.products.append(p)

    def mostrar_productos(self):
        for product in self.products:
            print(product)

    


