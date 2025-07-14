from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from abstract_clases.abscract_clases import WebScrapperDinamico

class AlkostoWebScrapper(WebScrapperDinamico):
    def __init__(self, objeto:str):
        super().__init__(objeto)
    
    def parsear_json(self):
        option= Options()
        option.add_argument("--headless")
        option.add_argument("--log-level=3")

        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://www.alkosto.com/search?text=audifonos")
        time.sleep(5)
    
    def buscar_nombre(self):
        names = self.driver.find_elements(By.XPATH, '//h3[contains(@class, "product__item__top__title") and @data-index]')
        self.names=[
            name.text for name in names
        ]
        print(self.names)

    def buscar_marca(self):
        marcas = self.driver.find_elements(By.CLASS_NAME, "product__item__information__brand")
        self.marcas=[
            marca.text for marca in marcas
        ]



