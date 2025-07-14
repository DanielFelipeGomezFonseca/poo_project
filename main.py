from real_clases.Fallabela_Scrapper import FallabelaScrapper
from real_clases.Panamericana_Scrapper import PanamericanaScrapper
from real_clases.Wikipedia_Scrapper import WikipediaScrapper
from real_clases.Alkosto_Scrapper import AlkostoWebScrapper

# Scrapper1=PanamericanaScrapper("audifonos")
# Scrapper1.parsear_json()
# Scrapper1.buscar_nombre()
# Scrapper1.buscar_precio()
# Scrapper1.buscar_marca()
# Scrapper1.buscar_link()
# Scrapper1.buscar_disponibilidad()
# Scrapper1.crear_productos()
# Scrapper1.mostrar_productos()

# Scrapper2=FallabelaScrapper ("teclado")
# Scrapper2.parsear_json()
# Scrapper2.buscar_nombre()
# Scrapper2.buscar_marca()
# Scrapper2.buscar_link()
# (Scrapper2.buscar_precio())
# Scrapper2.buscar_descuento()
# Scrapper2.crear_productos()
# Scrapper2.mostrar_productos()

# Scraper3=WikipediaScrapper("audifonos")
# Scraper3.parsear_pagina()
# Scraper3.obtener_nombre_pagina()
# Scraper3.obtener_titulos()
# Scraper3.obtener_parrafos()

scraper4=AlkostoWebScrapper("audifonos")
scraper4.parsear_json()
scraper4.buscar_marca()
scraper4.buscar_nombre()
