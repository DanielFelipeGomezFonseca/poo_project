from real_clases.Menu_Pages import MenuPages
from real_clases.Menu_Products import MenuProducts
from real_clases.Menu_Filters import MenuFilters
from real_clases.Menu_Filtered import MenuFiltered
from real_clases.Menu_Marcas import MenuMarcas
from real_clases.Menu_Filters_Price_Order import MenuFiltersPrice
from real_clases.Fallabela_Scrapper import FallabelaScrapper
from real_clases.Panamericana_Scrapper import PanamericanaScrapper
from real_clases.Wikipedia_Scrapper import WikipediaScrapper
from real_clases.Alkosto_Scrapper import AlkostoWebScrapper

menu_pages = MenuPages(["Panamericana","Fallabela","Alkosto"])
menu_pages.display()
selected_page = menu_pages.select()

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
    Scrapper1.crear_productos()
    menu_filters = MenuFilters(["Mostrar todos los productos","Filtrar"])
    menu_filters.display()
    selected_filter = menu_filters.select()

    if selected_filter == "filtrado":
        menu_filtered = MenuFiltered(["Marcas","Precios"])
        menu_filtered.display()
        selected_filtered = menu_filtered.select()

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

        if selected_filtered == "precio":
            prices = Scrapper1.compilar_precios()
            print(prices)
            menu_prices = MenuFiltersPrice(["Mayor a Menor","Menor a Menor","Precio Especifico"])
            menu_prices.display()
            selected_price = menu_prices.select()
            filtered_prices = []
            if selected_price == "maym":
                sorted_prod = sorted(Scrapper1.products, key=lambda p: p.precio, reverse=True)

                for producto in sorted_prod:
                    print(producto)

            if selected_price == "menm":
                sorted_prod = sorted(Scrapper1.products, key=lambda p: p.precio)

                for producto in sorted_prod:
                    print(producto)

            if selected_price == "esp":
                input_price = int(input("¿Que precio busca?: "))
                priced_prod = [product for product in Scrapper1.products if product.precio == input_price]
                for producto in priced_prod:
                    print(producto)

    if selected_filter == "todo":
        Scrapper1.mostrar_productos()

if selected_page == "Fallabela":
    menu_products = MenuProducts(["Audifonos","Mouses","Teclados"])
    menu_products.display()
    selected_product = menu_products.select()
    Scrapper2=FallabelaScrapper (selected_product)
    Scrapper2.parsear_json()
    Scrapper2.buscar_nombre()
    Scrapper2.buscar_marca()
    Scrapper2.buscar_link()
    Scrapper2.buscar_precio()
    Scrapper2.buscar_descuento()
    Scrapper2.crear_productos()
    menu_filters = MenuFilters(["Mostrar todos los productos","Filtrar"])
    menu_filters.display()
    selected_filter = menu_filters.select()

    if selected_filter == "filtrado":
        menu_filtered = MenuFiltered(["Marcas","Precios"])
        menu_filtered.display()
        selected_filtered = menu_filtered.select()

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

        if selected_filtered == "precio":
            prices = Scrapper2.compilar_precios()
            print(prices)
            menu_prices = MenuFiltersPrice(["Mayor a Menor","Menor a Menor","Precio Especifico"])
            menu_prices.display()
            selected_price = menu_prices.select()
            filtered_prices = []
            if selected_price == "maym":
                sorted_prod = sorted(Scrapper2.products, key=lambda p: p.precio, reverse=True)

                for producto in sorted_prod:
                    print(producto)

            if selected_price == "menm":
                sorted_prod = sorted(Scrapper2.products, key=lambda p: p.precio)

                for producto in sorted_prod:
                    print(producto)

            if selected_price == "esp":
                input_price = int(input("¿Que precio busca?: "))
                priced_prod = [product for product in Scrapper2.products if product.precio == input_price]
                for producto in priced_prod:
                    print(producto)

    if selected_filter == "todo":
        Scrapper2.mostrar_productos()

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
    scraper4.crear_productos()
    menu_filters = MenuFilters(["Mostrar todos los productos","Filtrar"])
    menu_filters.display()
    selected_filter = menu_filters.select()

    if selected_filter == "filtrado":
        menu_filtered = MenuFiltered(["Marcas","Precios"])
        menu_filtered.display()
        selected_filtered = menu_filtered.select()

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

        if selected_filtered == "precio":
            prices = scraper4.compilar_precios()
            print(prices)
            menu_prices = MenuFiltersPrice(["Mayor a Menor","Menor a Menor","Precio Especifico"])
            menu_prices.display()
            selected_price = menu_prices.select()
            filtered_prices = []
            if selected_price == "maym":
                sorted_prod = sorted(scraper4.products, key=lambda p: p.precio, reverse=True)

                for producto in sorted_prod:
                    print(producto)

            if selected_price == "menm":
                sorted_prod = sorted(scraper4.products, key=lambda p: p.precio)

                for producto in sorted_prod:
                    print(producto)

            if selected_price == "esp":
                input_price = int(input("¿Que precio busca?: "))
                priced_prod = [product for product in scraper4.products if product.precio == input_price]
                for producto in priced_prod:
                    print(producto)

    if selected_filter == "todo":
        scraper4.mostrar_productos()

# Scraper3=WikipediaScrapper("audifonos")
# Scraper3.parsear_pagina()
# Scraper3.obtener_nombre_pagina()
# Scraper3.obtener_titulos()
# Scraper3.obtener_parrafos()