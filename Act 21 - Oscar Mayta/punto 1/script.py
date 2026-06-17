"""
1-
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista de 5 enteros.
2) Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

def cargarlista():
    lista = []
    for x in range(5):
        valor = int(input(f"Ingresar el valor n°{x+1}: "))
        lista.append(valor)
    return lista

def mayormenor(lista):
    mayor = lista[0]
    menor = lista[0]

    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]

        if lista[x] < menor:
            menor = lista[x]

    return mayor, menor

lista = cargarlista()

mayor, menor = mayormenor(lista)

print("Mayor valor:", mayor)
print("Menor valor:", menor)