"""
4-
Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
 Diseñar un diccionario donde la Clave sea el identificador único del dron (ej:
&quot;DRON-01&quot;) y el Valor sea una lista de tuplas que almacene las coordenadas de
las paradas programadas: [(latitud, longitud)].
Desarrollar las siguientes funciones:
1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas
geográficas.
2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
de coordenadas asociadas.
3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad
de elementos).
"""

def cargar():

    registros = {}

    for i in range(3):
        dron = input(f"Ingrese el identificador del dron n°{i+1}: ")

        lista = []

        cantidad = int(input("Ingrese la cantidad de paradas: "))

        for j in range(cantidad):
            latitud = float(input(f"Ingrese la latitud de la parada n°{j+1}: "))
            longitud = float(input(f"Ingrese la longitud de la parada n°{j+1}: "))

            lista.append((latitud, longitud))

        registros[dron] = lista

    return registros


def listar(registros):

    print("Rutas de los drones:")

    for dron in registros:
        print("Dron:", dron)

        for latitud, longitud in registros[dron]:
            print("Coordenadas:", latitud, longitud)


def ruta_mas_larga(registros):

    mayor = 0
    dron_mayor = ""

    for dron in registros:

        cantidad = len(registros[dron])

        if cantidad > mayor:
            mayor = cantidad
            dron_mayor = dron

    print("El dron con la ruta mas larga es:", dron_mayor)
    print("Cantidad de paradas:", mayor)


registros = cargar()
listar(registros)
ruta_mas_larga(registros)