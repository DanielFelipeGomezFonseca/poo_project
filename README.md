# Nombre del equipo-Alternativa definida: Serial Experiments POO - Alternativa 2

# Nombre del proyecto: Search While Rest
![SWR (1)](https://github.com/user-attachments/assets/3dbf9bf8-18ad-4aa4-a1c9-bf91d8fc4b99)

## Descripción del Proyecto

Este proyecto consiste en una aplicación basada en un sistema de web scraping, cuyo objetivo es filtrar la búsqueda de periféricos para computadoras de acuerdo con los criterios y preferencias proporcionados por el usuario. Los perifericos en especifico seran los audifonos, los teclados y los "mouse"

![image](https://github.com/user-attachments/assets/cec8574b-b474-40e8-82ab-ebd3df3330b4)

Las variables que se tienen en cuenta son:

- Precio

- Marca

- Modelo

- Disponibilidad

- Descuento (si aplica)


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
}

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

## Solucion Definitiva :v
Se mostraran aspectos importantes de la solucion definitiva:
### Panamericana Scrapper: 
La funcion mas importante se presenta a continuacion, esta funcion busca el json de "respuesta" que da la pagina luego de conectarse. Para esto se usan las librerias Request y BeatifulSoup debido a que puedo hallar la API que la pagina pide al solicitar datos al servidor.   
```python

 def parsear_json(self) -> None:
        self.__data = []
        if self._objeto == "audifonos":
            url = "https://www.panamericana.com.co/audifonos?_q=audifonos&map=ft&"
        elif self._objeto == "mouse":
            url = "https://www.panamericana.com.co/mouse?_q=mouse&map=ft&"
        elif self._objeto == "teclado":
            url = "https://www.panamericana.com.co/teclado?_q=teclado&map=ft&"
        try:
            page = 1
            ####? Se usa un while True para recorrer pagina por pagina 
            while True:
                print(f"Scrapeando pagina {page}")
                url_modified = url + f"page={page}"
                response = requests.get(url_modified, timeout=10)

                if response.status_code != 200:
                    raise ConnectionError("No se pudo conectar")
                soup = BeautifulSoup(response.text, "lxml")
                scripts = soup.find_all("script", type="application/ld+json")

                #! En esta seccion de codigo se encuentra el BREAK, el detalle de eso esta en el github
                try:
                    raw_data = json.loads(scripts[1].string)
                except IndexError:
                    print(f"La pagina {page - 1} es la ultima pagina")
                    break

                self.__data.append(raw_data)
                page += 1

        except (requests.exceptions.Timeout, requests.exceptions.ConnectTimeout) as error:
            print(f"Existe este {error}")
        except KeyboardInterrupt as f_error:
            print(f"{f_error}")

```
Imagen de la structura Json de PANAMERICANA
<img width="1453" height="641" alt="image" src="https://github.com/user-attachments/assets/428cc6c7-53dd-4ba4-99d1-d69d7ab09cbd" />

Un problema que sucedio es que los productos estan separados por paginas, es decir distintos links con un numero distinto, entonces para esto se aplica la funcion WHILE, que con un contador va recorriendo cada pagina. Es importante mencionar que el Break, se hizo asi porque normalemente request saca dos scripts, pero cuando la pagina no contiene productos el segundo script (por eso el indice [1]), entonces asi identifico cual #page tenia los elementos. 

###  Excepciones
Se usan excepciones en todas las funciones, por si ocurre un error no se afecta el parseo (en especial la primera funcion, la mas importante) Existen algunas respuestas personalizadas de la libreria request.

### Python y las List_C
Para implementar las funciones que buscan cierto tipo de datos, se uso list_C, esto se debe a que luego de hacer el codigo con varios for, se reflexiono de la facilidad que las List_C daban. Posteriomente se muestra una comparacion tomando como ejemplo la funcion Buscar_Precio

### List_c
```python

    def buscar_precio(self) -> list:
        try:
            self.__precios = [
                item["price"]
                for Json in self.__data
                for product in Json["itemListElement"]
                for item in product["item"]["offers"]["offers"]
            ]
        except Exception as error:
            print(f"Hay error {error}")
```

### No List_C
```python

def buscar_precio(self) -> list:
        self.precios = []
        try:
            for Json in self.data:
                d_1 = Json["itemListElement"]
                for product in d_1:
                    self.second_step = product["item"]
                    third_step = self.second_step["offers"]
                    fourth_step = third_step["offers"]
                    for item in fourth_step:
                        price = item["price"]
                    self.precios.append(price)
        except Exception as error:
            print(f"Hay error {error}")
```
### Fallabela Scrapper: 
Con fallabela tambien sucede algo similar a panamericana, busco la API que la pagina genera al solicitar los datos al servidor 
