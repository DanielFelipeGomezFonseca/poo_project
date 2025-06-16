import requests
from bs4 import BeautifulSoup
import json

class WebScrapper:
    def __init__(self,object):
       self._object = object

    def parsear_json(self):
       pass

    def buscar_nombre(self):
       pass

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
