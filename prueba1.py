from collections import namedtuple

Producto = namedtuple('Producto', ['nombre', 'precio', 'categoria'])

nombres = ['Manzana', 'Pera', 'Uva']
precios = [1000, 2000, 1500]
categorias = ['Fruta', 'Fruta', 'Fruta']

productos = []

for i in range(len(nombres)):
    p = Producto(nombres[i], precios[i], categorias[i])
    productos.append(p)

# Ejemplo de uso:
for p in productos:
    print(p.nombre, p.precio, p.categoria)
