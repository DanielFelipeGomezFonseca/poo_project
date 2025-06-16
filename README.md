# Nombre del equipo-Alternativa definida: Serial Experiments POO - Alternativa 2

# Nombre del proyecto: Search While Rest
![SWR (1)](https://github.com/user-attachments/assets/3dbf9bf8-18ad-4aa4-a1c9-bf91d8fc4b99)

## Descripción del Proyecto

Este proyecto consiste en una aplicación basada en un sistema de web scraping, cuyo objetivo es filtrar la búsqueda de periféricos para computadoras de acuerdo con los criterios y preferencias proporcionados por el usuario. Los perifericos en especifico seran los audifonos, los teclados y los "mouse"

![image](https://github.com/user-attachments/assets/cec8574b-b474-40e8-82ab-ebd3df3330b4)

Las variables que se tienen en cuenta son:

- Precio

- Empresa fabricante

- Modelo

- Año de lanzamiento

- Funcionalidades


La aplicación facilita la búsqueda de productos para el usuario. Para ello, realiza la recolección de datos desde plataformas de comercio electrónico como Alkosto,   Panamericana.


## Por que se eligio

En algunas ocaciones se pierde mucho tiempo al buscar este tipo de perifericos, puesto que en cada pagina los precios varian, y pueden haber descuento o cobrar por envio, es por esto que es mejor hacer un "scrapper" que pueda ahorrar tiempo a este tipo de productos. 
![image](https://github.com/user-attachments/assets/1e49e1f9-ec8f-417a-b000-44348ff5b7c1)



## Diagrama de Clase 1: Funcionamiento del scrapper

```mermaid
---
title: Scrapers
---
classDiagram

class Producto {
  #nombre: str
  #precio: float
  #marca: str
  #url: str
  #plataforma: str
  #descuento: float

  +__init__() 
  +__str__() 
}

class Scraper {
  <<abstract>>
  #objeto_scrapear: str

  __init__(objeto_scrapear: str) 
  +parsear_json() -> Json
  +buscar_nombre() -> str
  +buscar_marca() -> str
  +buscar_precio() -> float
  +buscar_descuentos() -> float
  +crear_producto() -> Producto
  +guardar_producto(p: Producto) -> list[Producto]


class AlkostoScraper {
  __init__() 
}

class PanamericanaScraper {
  __init__() 
}

Scraper <|-- AlkostoScraper
Scraper <|-- PanamericanaScraper
```
## Diagrama de Clase 2: Relacion con el usario
```mermaid

---
title: Filtro y Usuario
---
classDiagram

class Producto {
  #nombre: str
  #precio: float
  #marca: str
  #url: str
  #plataforma: str
  #descuento: float

  __init__() 
  __str__() 
}

class Filtro {
  #productos_filtrar: list[Producto]
  #parametros_filtrar: dict

  __init__(productos: list[Producto], parametros: dict) 
  +filtrar_por_nombres() -> list[Producto]
  +filtrar_por_marcas() -> list[Producto]
  +filtrar_por_precios() -> list[Producto]
  +filtrar_por_descuento() -> list[Producto]
}

class MostrarProductos {
  #filtro: Filtro

  __init__(filtro: Filtro) 
  +escribir_productos() 
  +mostrar_productos() 
}


Filtro --> Producto : usa
MostrarProductos --> Filtro : usa
Usuario --> MostrarProductos : usa

```

## Solucion preliminar
El formato al que se quiere parsear toda la informacion es el formato tipo Json:
Porque? 
Porque es un formato muy facil de entender, de manejar y es el formato defecto de las APIs :)

Uso de librerias: Request, Beatiful Soap, Selenium:
-Requests: se usa para obtener el contenido de la web haciendo una peticion  HTTP, y luego poderlo parsear usando otra libreria. Esta libreria es muy buena y muy confiable

-BeatifulSoap: Esto se usa para parsear las paginas web, es decir para  analizar y extraer el json del html, en caso de que se nescecite. La libreria es ampliamente utilizada y recomendada, ademas no es dificil de utilizar

-Selenium: Se usa para controlar a un navegador desde Python (depende de lo que la pagina pida)


![image](https://github.com/user-attachments/assets/f0bc22d3-32f3-49e6-8bd5-ee8c62c06a5b)

Con beautiful soap la idea es hallar y extraer estos scrips que contienen toda la informacion, aqui se muestra el ejemplo con panamericana
![image](https://github.com/user-attachments/assets/36c573f7-e729-452b-b1bd-ef379530cef2)

