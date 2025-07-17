from bs4 import BeautifulSoup
from collections import namedtuple
import requests
import json

from abstract_clases.abscract_clases import WebScrapperEstatico


class WikipediaScrapper(WebScrapperEstatico):
    def __init__(self, objeto):
        super().__init__(objeto)
        self.pagina = "Wikipedia"
    
    #! Funcion mas importante
    def parsear_pagina(self):
        if self._objeto == "audifonos":
            url = "https://es.wikipedia.org/wiki/Audífono"
        elif self._objeto == "mouse":
            url = "https://es.wikipedia.org/wiki/Ratón_(informática)"
        elif self._objeto == "teclado":
            url = "https://es.wikipedia.org/wiki/Teclado_(informática)"

        self.response = requests.get(url, timeout=10)
        if self.response.status_code != 200:
            raise ConnectionError("No se pudo conectar")  
        self.soup=BeautifulSoup(self.response.text, "html.parser")
  
    #! Uso List_C
    def obtener_nombre_pagina(self):
        name=self.soup.find(id="firstHeading")
        self.name=name.string

    def obtener_titulos(self):
        tittles=self.soup.find_all(["h2"])
        self.titles=[
            tittle.text.strip()
            for tittle in tittles
        ]

    def obtener_parrafos(self):
        paragraphs=self.soup.find_all("p")
        self.paragraphs=[
            paragraph.text.strip()
            for paragraph in paragraphs
        ]
 
    #! Guardo info en un JSON
    def crear_json(self):
        self.dict={"Titulo": self.name, "Cabezales": self.titles , "Parrafos": self.paragraphs}
    
    def mostrar_json(self):
        print(self.dict)
