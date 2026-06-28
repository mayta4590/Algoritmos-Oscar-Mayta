"""
4-
Un observatorio astronómico registra los descubrimientos de nuevos planetas
fuera del sistema solar.
 Diseñar un diccionario donde la Clave sea el nombre científico del
exoplaneta (ej: &quot;Kepler-22b&quot;) y el Valor sea una tupla con sus datos:
(distancia_anios_luz, tipo_de_atmosfera, es_habitable_booleano).
Desarrollar las siguientes funciones:
1. Cargar catálogo: Registrar por teclado la información de 4 exoplanetas
descubiertos.
2. Buscar exoplaneta: Permitir al usuario ingresar el nombre de un
exoplaneta por teclado. Si el exoplaneta se encuentra en el diccionario
(utilizando el operador in), mostrar todos sus detalles físicos y si reúne
condiciones de habitabilidad. De lo contrario, mostrar un cartel indicando:
&quot;El exoplaneta no figura en el catálogo actual&quot;.
3. Reportar Habitables: Mostrar en pantalla únicamente los nombres de los
exoplanetas cargados que fueron marcados como habitables.
"""

def cargar():
    exoplanetas = {}

    for i in range(4):
        nombre = input("Ingrese el nombre del exoplaneta: ")
        distancia = float(input("Ingrese la distancia en años luz: "))
        atmosfera = input("Ingrese el tipo de atmósfera: ")
        habitable = input("¿Es habitable? (True/False): ") == "True"

        exoplanetas[nombre] = (distancia, atmosfera, habitable)

    return exoplanetas


def buscar(exoplanetas):
    nombre = input("Ingrese el nombre del exoplaneta: ")

    if nombre in exoplanetas:
        print("Distancia:", exoplanetas[nombre][0], "años luz")
        print("Atmósfera:", exoplanetas[nombre][1])
        print("Habitable:", exoplanetas[nombre][2])
    else:
        print("El exoplaneta no figura en el catálogo actual")


def reportar_habitables(exoplanetas):
    print("Exoplanetas habitables:")

    for nombre in exoplanetas:
        if exoplanetas[nombre][2] == True:
            print(nombre)


exoplanetas = cargar()
buscar(exoplanetas)
reportar_habitables(exoplanetas)