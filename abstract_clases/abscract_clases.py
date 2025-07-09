class WebScrapper:
    def __init__(self, objeto: str):
        self._objeto = objeto

class WebScrapperEstatico(WebScrapper):
    def __init__(self, objeto):
        super().__init__(objeto)

    def parsear_pagina(self):
        pass

    def obtener_nombre_pagina(self):
        pass

    def obtener_titulos(self):
        pass

    def obtener_parrafos(self):
        pass
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

    def buscar_descuento(self):
        pass

    def buscar_disponibilidad(self):
        pass

    def crear_productos(self):
        pass

    def mostrar_productos(self):
        pass