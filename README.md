# Nombre del Proyecto

## Descripción del Proyecto

Este proyecto consiste en una aplicación basada en un sistema de web scraping, cuyo objetivo es filtrar la búsqueda de periféricos para computadoras de acuerdo con los criterios y preferencias proporcionados por el usuario. Los perifericos en especifico seran los audifonos, los teclados y los "mouse"

Las variables que se tienen en cuenta son:

- Precio

- Empresa fabricante

- Modelo

- Año de lanzamiento

- Funcionalidades


La aplicación facilita la búsqueda de productos para el usuario. Para ello, realiza la recolección de datos desde plataformas de comercio electrónico como MercadoLibre, Ebay, Panamericana.


## Por que se eligio

En algunas ocaciones se pierde mucho tiempo al buscar este tipo de perifericos, puesto que en cada pagina los precios varian, y pueden haber descuento o cobrar por envio, es por esto que es mejor hacer un "scrapper" que pueda ahorrar tiempo a este tipo de productos. 
![image](https://github.com/user-attachments/assets/1e49e1f9-ec8f-417a-b000-44348ff5b7c1)



## Diagrama de Clases

```mermaid
classDiagram

class Producto {
  - String nombre
  - float precio
  - String marca
  - bool envio_gratis
  - String url
  - String plataforma
}

class Scraper {
  <<abstract>>
  + List~Producto~ extraer_productos(String tipo)
}

class EbayScraper {
  + List~Producto~ extraer_productos(String tipo)
}

class MercadoLibreScraper {
  + List~Producto~ extraer_productos(String tipo)
}

class Filtro {
  + List~Producto~ filtrar(List~Producto~, Dict criterios)
}

class BuscadorProductos {
  - List~Scraper~ scrapers
  + List~Producto~ buscar(String tipo, Dict criterios)
}

Scraper <|-- EbayScraper
Scraper <|-- MercadoLibreScraper

BuscadorProductos --> Scraper : usa
BuscadorProductos --> Filtro : usa
Filtro --> Producto : filtra
Scraper --> Producto : extrae
```
