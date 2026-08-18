"""
1-
Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes de
dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
monitoreo (ej: &quot;San Telmo&quot;) y el Valor sea una lista de flotantes que represente
las últimas 3 lecturas de contaminación tomadas en el día.
Desarrollar las siguientes funciones:
1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada
barrio.
3. Alerta ambiental: Mostrar en pantalla una alerta roja de &quot;Protocolo de
Emergencia&quot; únicamente para las estaciones cuyo promedio de contaminación
supere las 400 ppm.
"""

def cargar():

    registros = {}

    for i in range(3):
        estacion = input(f"Ingrese el nombre de la estacion n°{i+1}: ")

        lista = []

        for j in range(3):
            lectura = float(input(f"Ingrese la lectura de CO2 n°{j+1}: "))
            lista.append(lectura)

        registros[estacion] = lista

    return registros


def listar(registros):

    print("Promedio de contaminacion:")

    for estacion in registros:
        total = 0

        for lectura in registros[estacion]:
            total = total + lectura

        promedio = total / 3

        print("Estacion:", estacion)
        print("Promedio:", promedio, "ppm")


def alerta(registros):

    for estacion in registros:
        total = 0

        for lectura in registros[estacion]:
            total = total + lectura

        promedio = total / 3

        if promedio > 400:
            print("ALERTA ROJA - Protocolo de Emergencia")
            print("Estacion:", estacion)


registros = cargar()
listar(registros)
alerta(registros)