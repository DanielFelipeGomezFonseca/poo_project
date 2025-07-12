from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from abstract_clases.abscract_clases import WebScrapperDinamico

class AlkostoWebScrapper(WebScrapperDinamico):
    def __init__(self, objeto:str):
        super().__init__(objeto)
    
    def parsear_json(self):

        driver = webdriver.Chrome()
        driver.get("https://www.alkosto.com/search?text=audifonos")
        time.sleep(5)
        job_list = driver.find_elements_by_xpath("//div[@data-tn-component='organicJob']")
        print(job_list)



