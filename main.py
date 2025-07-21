from real_clases.Menu_Pages import MenuPages
from real_clases.Menu_Products import MenuProducts
from real_clases.Menu_Filters import MenuFilters
from real_clases.Menu_Filtered import MenuFiltered
from real_clases.Menu_Marcas import MenuMarcas
from real_clases.Menu_Filters_Price_Order import MenuFiltersPrice
from real_clases.Fallabela_Scrapper import FallabelaScrapper
from real_clases.Panamericana_Scrapper import PanamericanaScrapper
from real_clases.Alkosto_Scrapper import AlkostoWebScrapper
from real_clases.Wikipedia_Scrapper import WikipediaScrapper
import json

menu_pages = MenuPages(["Panamericana","Fallabela","Alkosto"])
menu_pages.display()
selected_page = menu_pages.select()

# Condicional en el que se ejecuta todos los procesos relacionados con Panamericana
if selected_page == "Panamericana":
    menu_products = MenuProducts(["Audifonos","Mouses","Teclados"])
    menu_products.display()
    selected_product = menu_products.select()
    print(selected_product)
    Scrapper1=PanamericanaScrapper(selected_product)
    Scrapper1.parsear_json()
    Scrapper1.buscar_nombre()
    Scrapper1.buscar_precio()
    Scrapper1.buscar_marca()
    Scrapper1.buscar_link()
    Scrapper1.buscar_disponibilidad()
    product_list = Scrapper1.crear_productos()
    opt = ["Si","No"]
    for i in range(len(opt)):
        print(str(i+1),opt[i])
    wikipedia_check = input("¿Quieres saber más sobre el producto?: ")
    if wikipedia_check == "1": # Condicional que da paso al scrapping de Wikipedia
        wikipedia_scrapper = WikipediaScrapper(selected_product)
        wikipedia_scrapper.parsear_pagina()
        wikipedia_scrapper.obtener_nombre_pagina()
        wikipedia_scrapper.obtener_titulos()
        wikipedia_scrapper.obtener_parrafos()
        wikipedia_scrapper.crear_json()
        wikipedia_scrapper.mostrar_json()
    menu_filters = MenuFilters(["Mostrar todos los productos","Filtrar"])
    menu_filters.display()
    selected_filter = menu_filters.select()

# Condicional que ejecuta todas las funciones relacionadas a filtros
    if selected_filter == "filtrado":
        menu_filtered = MenuFiltered(["Marcas","Precios"])
        menu_filtered.display()
        selected_filtered = menu_filtered.select()

# Funciones para filtrar MARCAS
        if selected_filtered == "marca":
            marcas = Scrapper1.compilar_marcas()
            menu_marcas = MenuMarcas(marcas)
            menu_marcas.display()
            selected_marca = menu_marcas.select(marcas)
            filtered_products = []

            for product in Scrapper1.products:
                if product.marca == selected_marca:
                    filtered_products.append(product)

            for p in filtered_products:
                print(p)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in filtered_products]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

# Funciones para filtrar PRECIOS
        if selected_filtered == "precio":
            prices = Scrapper1.compilar_precios()
            print(prices)
            menu_prices = MenuFiltersPrice(["Mayor a Menor","Menor a Mayor","Precio Especifico"])
            menu_prices.display()
            selected_price = menu_prices.select()
            filtered_prices = []

            if selected_price == "maym": # Mayor a Menor
                sorted_prod = sorted(Scrapper1.products, key=lambda p: p.precio, reverse=True)
                for producto in sorted_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in sorted_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

            if selected_price == "menm": # Menor a Mayor
                sorted_prod = sorted(Scrapper1.products, key=lambda p: p.precio)
                for producto in sorted_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in sorted_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

            if selected_price == "esp": # Buscar precio en específico
                input_price = int(input("¿Que precio busca?: "))
                priced_prod = [product for product in Scrapper1.products if product.precio == input_price]
                for producto in priced_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in priced_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

# Codigo que se ejecuta si no se aplica ningun filtro
    if selected_filter == "todo":
        for i in product_list:
            print(i)
        opt = ["Si","No"]
        for i in range(len(opt)):
            print(str(i+1),opt[i])
        save_option = input("¿Deseas guardar toda esta información?: ")
        if save_option == "1":
            data_export = [prod._asdict() for prod in product_list]
            with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                json.dump(data_export, f, ensure_ascii=False, indent=4)

# Condicional en el que se ejecuta todos los procesos relacionados con Fallabela
if selected_page == "Fallabela":
    menu_products = MenuProducts(["Audifonos","Mouses","Teclados"])
    menu_products.display()
    selected_product = menu_products.select()
    Scrapper2=FallabelaScrapper (selected_product) # Scrapping de Fallabela
    Scrapper2.parsear_json()
    Scrapper2.buscar_nombre()
    Scrapper2.buscar_marca()
    Scrapper2.buscar_link()
    Scrapper2.buscar_precio()
    Scrapper2.buscar_descuento()
    product_list = Scrapper2.crear_productos()
    opt = ["Si","No"]
    for i in range(len(opt)):
        print(str(i+1),opt[i])
    wikipedia_check = input("¿Quieres saber más sobre el producto?: ")
    if wikipedia_check == "1": # Condicional que da paso al scrapping de Wikipedia
        wikipedia_scrapper = WikipediaScrapper(selected_product)
        wikipedia_scrapper.parsear_pagina()
        wikipedia_scrapper.obtener_nombre_pagina()
        wikipedia_scrapper.obtener_titulos()
        wikipedia_scrapper.obtener_parrafos()
        wikipedia_scrapper.crear_json()
        wikipedia_scrapper.mostrar_json()
    menu_filters = MenuFilters(["Mostrar todos los productos","Filtrar"])
    menu_filters.display()
    selected_filter = menu_filters.select()

# Condicional que ejecuta todas las funciones relacionadas a filtros
    if selected_filter == "filtrado":
        menu_filtered = MenuFiltered(["Marcas","Precios"])
        menu_filtered.display()
        selected_filtered = menu_filtered.select()

# Funciones para filtrar MARCAS
        if selected_filtered == "marca":
            marcas = Scrapper2.compilar_marcas()
            menu_marcas = MenuMarcas(marcas)
            menu_marcas.display()
            selected_marca = menu_marcas.select(marcas)
            filtered_products = []

            for product in Scrapper2.products:
                if product.marca == selected_marca:
                    filtered_products.append(product)

            for p in filtered_products:
                print(p)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in filtered_products]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

# Funciones para filtrar PRECIOS
        if selected_filtered == "precio":
            prices = Scrapper2.compilar_precios()
            print(prices)
            menu_prices = MenuFiltersPrice(["Mayor a Menor","Menor a Menor","Precio Especifico"])
            menu_prices.display()
            selected_price = menu_prices.select()
            filtered_prices = []

            if selected_price == "maym": # Mayor a Menor
                sorted_prod = sorted(Scrapper2.products, key=lambda p: p.precio, reverse=True)
                for producto in sorted_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in sorted_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

            if selected_price == "menm": # Menor a Mayor
                sorted_prod = sorted(Scrapper2.products, key=lambda p: p.precio)
                for producto in sorted_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in sorted_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

            if selected_price == "esp": # Buscar precio específico
                input_price = int(input("¿Que precio busca?: "))
                priced_prod = [product for product in Scrapper2.products if product.precio == input_price]
                for producto in priced_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in priced_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

# Codigo que se ejecuta si no se aplica ningun filtro
    if selected_filter == "todo":
        for i in product_list:
            print(i)
        opt = ["Si","No"]
        for i in range(len(opt)):
            print(str(i+1),opt[i])
        save_option = input("¿Deseas guardar toda esta información?: ")
        if save_option == "1":
            data_export = [prod._asdict() for prod in product_list]
            with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                json.dump(data_export, f, ensure_ascii=False, indent=4)

# Condicional en el que se ejecuta todos los procesos relacionados con Alkosto
if selected_page == "Alkosto":
    menu_products = MenuProducts(["Audifonos"])
    menu_products.display()
    selected_product = menu_products.select()
    scraper4 = AlkostoWebScrapper(selected_product)
    scraper4.parsear_json()
    scraper4.buscar_nombre()
    scraper4.buscar_marca()
    scraper4.buscar_link()
    scraper4.buscar_precio()
    scraper4.buscar_descuento()
    product_list = scraper4.crear_productos()
    opt = ["Si","No"]
    for i in range(len(opt)):
        print(str(i+1),opt[i])
    wikipedia_check = input("¿Quieres saber más sobre el producto?: ")
    if wikipedia_check == "1":
        wikipedia_scrapper = WikipediaScrapper(selected_product)
        wikipedia_scrapper.parsear_pagina()
        wikipedia_scrapper.obtener_nombre_pagina()
        wikipedia_scrapper.obtener_titulos()
        wikipedia_scrapper.obtener_parrafos()
        wikipedia_scrapper.crear_json()
        wikipedia_scrapper.mostrar_json()
    menu_filters = MenuFilters(["Mostrar todos los productos","Filtrar"])
    menu_filters.display()
    selected_filter = menu_filters.select()

# Condicional que ejecuta todas las funciones relacionadas a filtros
    if selected_filter == "filtrado":
        menu_filtered = MenuFiltered(["Marcas","Precios"])
        menu_filtered.display()
        selected_filtered = menu_filtered.select()

# Funciones para filtrar MARCAS
        if selected_filtered == "marca":
            marcas = scraper4.compilar_marcas()
            menu_marcas = MenuMarcas(marcas)
            menu_marcas.display()
            selected_marca = menu_marcas.select(marcas)
            filtered_products = []

            for product in scraper4.products:
                if product.marca == selected_marca:
                    filtered_products.append(product)

            for p in filtered_products:
                print(p)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in filtered_products]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

# Funciones para filtrar PRECIOS
        if selected_filtered == "precio":
            prices = scraper4.compilar_precios()
            print(prices)
            menu_prices = MenuFiltersPrice(["Mayor a Menor","Menor a Menor","Precio Especifico"])
            menu_prices.display()
            selected_price = menu_prices.select()
            filtered_prices = []

            if selected_price == "maym": # Mayor a Menor
                sorted_prod = sorted(scraper4.products, key=lambda p: p.precio, reverse=True)
                for producto in sorted_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in sorted_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

            if selected_price == "menm": # Menor a Mayor
                sorted_prod = sorted(scraper4.products, key=lambda p: p.precio)
                for producto in sorted_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in sorted_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

            if selected_price == "esp": # Buscar precio específico
                input_price = int(input("¿Que precio busca?: "))
                priced_prod = [product for product in scraper4.products if product.precio == input_price]
                for producto in priced_prod:
                    print(producto)
                opt = ["Si","No"]
                for i in range(len(opt)):
                    print(str(i+1),opt[i])
                save_option = input("¿Deseas guardar toda esta información?: ")
                if save_option == "1":
                    data_export = [prod._asdict() for prod in priced_prod]
                    with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                        json.dump(data_export, f, ensure_ascii=False, indent=4)

# Codigo que se ejecuta si no se aplica ningun filtro
    if selected_filter == "todo":
        for i in product_list:
            print(i)
        opt = ["Si","No"]
        for i in range(len(opt)):
            print(str(i+1),opt[i])
        save_option = input("¿Deseas guardar toda esta información?: ")
        if save_option == "1":
            data_export = [prod._asdict() for prod in product_list]
            with open(f'{selected_product}_exportados.json', 'w', encoding='utf-8') as f:
                json.dump(data_export, f, ensure_ascii=False, indent=4)
