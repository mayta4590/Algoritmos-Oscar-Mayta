"""
3-
Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
en cada habitación de la casa.
 Crear un diccionario donde la Clave sea el nombre del ambiente (ej: &quot;Cocina&quot;,
&quot;Dormitorio&quot;) y el Valor sea una lista de tuplas, donde cada tupla represente un
dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
Desarrollar las siguientes funciones:
1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
operador decida no cargar más para ese ambiente.
2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
en Watts acumulado en cada una de ellas.
3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
energía consume de toda la casa (el valor máximo individual dentro de todas las
listas del diccionario), indicando en qué habitación se encuentra.
"""

def cargar():

    registros = {}

    for i in range(3):
        habitacion = input(f"Ingrese el nombre del ambiente n°{i+1}: ")
        lista = []

        seguir = "si"

        while seguir == "si":
            dispositivo = input("Ingrese el nombre del dispositivo: ")
            consumo = int(input("Ingrese el consumo en Watts: "))

            lista.append((dispositivo, consumo))

            seguir = input("¿Desea ingresar otro dispositivo? si/no: ")

        registros[habitacion] = lista

    return registros


def listar(registros):

    print("Consumo de las habitaciones:")

    for habitacion in registros:
        total = 0

        for dispositivo, consumo in registros[habitacion]:
            total = total + consumo

        print("Habitacion:", habitacion)
        print("Consumo total:", total, "Watts")


def dispositivo_critico(registros):

    mayor = 0
    dispositivo_mayor = ""
    habitacion_mayor = ""

    for habitacion in registros:
        for dispositivo, consumo in registros[habitacion]:

            if consumo > mayor:
                mayor = consumo
                dispositivo_mayor = dispositivo
                habitacion_mayor = habitacion

    print("El dispositivo que mas consume es:", dispositivo_mayor)
    print("Se encuentra en:", habitacion_mayor)
    print("Su consumo es de:", mayor, "Watts")


registros = cargar()
listar(registros)
dispositivo_critico(registros)