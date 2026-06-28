"""
3-
Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
 Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: &quot;192.168.1.50&quot;) y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos).
"""

def cargar():
    registros = {}

    for i in range(4):
        ip = input("Ingrese la dirección IP: ")
        dispositivo = input("Ingrese el nombre del dispositivo: ")
        intentos = int(input("Ingrese la cantidad de intentos fallidos: "))

        registros[ip] = (dispositivo, intentos)

    return registros


def listar(registros):
    print("Lista de amenazas:")

    for ip in registros:
        print(ip, registros[ip][0], registros[ip][1])


def filtrar(registros):
    print("IPs que deben ser bloqueadas:")

    for ip in registros:
        if registros[ip][1] > 5:
            print(ip, registros[ip][0], registros[ip][1])


registros = cargar()
listar(registros)
filtrar(registros)