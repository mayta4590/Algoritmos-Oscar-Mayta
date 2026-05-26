"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""
nombres = []
ventas = []

for x in range(5):

    nom = input("Ingrese el nombre del vendedor: ")
    nombres.append(nom)

    venta = float(input("Ingrese el total vendido: "))
    ventas.append(venta)

for k in range(4):

    for x in range(4-k):

        if ventas[x] < ventas[x+1]:

            auxventa = ventas[x]
            ventas[x] = ventas[x+1]
            ventas[x+1] = auxventa

            auxnombre = nombres[x]
            nombres[x] = nombres[x+1]
            nombres[x+1] = auxnombre

print("\nLista ordenada de vendedores y ventas:")

for x in range(5):
    print(nombres[x], "-", ventas[x])

print("\nEl vendedor que menos vendió fue:")
print(nombres[4], "-", ventas[4])