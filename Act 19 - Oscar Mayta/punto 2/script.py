"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def cargar_sueldos():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese sueldo: "))
        lista.append(valor)
    return lista


def imprimir_sueldos(lista):
    print("Lista completa de sueldos")
    for x in range(len(lista)):
        print(lista[x])


def sueldo4000(lista):
    cont4000 = 0
    for x in range(len(lista)):
        if lista[x] > 4000:
            cont4000 = cont4000 + 1

    print("Cantidad de sueldos mayores a 4000:", cont4000)


def retornar_promedio(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]

    promedio = suma / len(lista)
    return promedio


def debajo_promedio(lista, promedio):
    print("Sueldos por debajo del promedio")
    for x in range(len(lista)):
        if lista[x] < promedio:
            print(lista[x])


sueldos = cargar_sueldos()

imprimir_sueldos(sueldos)

sueldo4000(sueldos)

promedio = retornar_promedio(sueldos)
print("Promedio de los sueldos:", promedio)

debajo_promedio(sueldos, promedio)