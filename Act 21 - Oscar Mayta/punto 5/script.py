"""
5-
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""

def cargar_productos():
    productos = []

    for x in range(5):
        nombre = input(f"Ingrese el nombre del producto {x+1}: ")
        precio = float(input("Ingrese el precio: "))

        productos.append((nombre, precio))

    return productos


def listar_productos(productos):
    print("\nListado de productos:")
    
    for producto in productos:
        print("Producto:", producto[0], "- Precio:", producto[1])


def productos_entre_10_y_15(productos):
    print("\nProductos con precios entre 10 y 15:")

    for producto in productos:
        if 10 <= producto[1] <= 15:
            print(producto[0], "-", producto[1])


productos = cargar_productos()

listar_productos(productos)

productos_entre_10_y_15(productos)