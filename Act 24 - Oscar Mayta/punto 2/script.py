"""
2-
En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
para realizar misiones cooperativas.
 Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej:
&quot;DragonesDeFuego&quot;) y el Valor sea una lista de cadenas con los nombres de
los jugadores (nicknames) que lo integran.
Desarrollar las siguientes funciones:
1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
preguntar cuántos integrantes posee para cargar sus respectivos nombres de
usuario en la lista interna.
2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
de miembros que posee cada uno.
3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
&quot;Solitario&quot; (no pertenece a ningún clan).
"""

def cargar():

    registros = {}

    for i in range(3):
        gremio = input(f"Ingrese el nombre del gremio n°{i+1}: ")

        lista = []

        cantidad = int(input("Ingrese la cantidad de integrantes: "))

        for j in range(cantidad):
            jugador = input(f"Ingrese el nombre del jugador n°{j+1}: ")
            lista.append(jugador)

        registros[gremio] = lista

    return registros


def listar(registros):

    print("Lista de gremios:")

    for gremio in registros:
        cantidad = len(registros[gremio])

        print("Gremio:", gremio)
        print("Cantidad de integrantes:", cantidad)


def buscar_jugador(registros):

    jugador_buscado = input("Ingrese el nombre del jugador que desea buscar: ")

    encontrado = False

    for gremio in registros:
        for jugador in registros[gremio]:

            if jugador == jugador_buscado:
                print("El jugador pertenece al gremio:", gremio)
                encontrado = True

    if encontrado == False:
        print("El jugador es Solitario")


registros = cargar()
listar(registros)
buscar_jugador(registros)