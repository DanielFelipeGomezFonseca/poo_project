# Nombre del Proyecto

## Descripción del Proyecto

Este proyecto consiste en una aplicación basada en un sistema de web scraping, cuyo objetivo es filtrar la búsqueda de periféricos para computadoras de acuerdo con los criterios y preferencias proporcionados por el usuario.

Las variables que se tienen en cuenta son:

- Precio

- Empresa fabricante

- Modelo

- Año de lanzamiento

- Compatibilidad

- Funcionalidades

- Software incluido (si aplica)

La aplicación facilita la búsqueda de productos ideales para el usuario, garantizando una buena relación calidad-precio. Para ello, realiza la recolección de datos desde plataformas de comercio electrónico como MercadoLibre y Amazon.

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