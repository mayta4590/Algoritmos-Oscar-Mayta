"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def cargardatos(lista):
    for x in range(10):
        elemento=int(input(f"Ingrese el elemnto n°{x+1}: "))
        lista.append(elemento)


def doslistas(lista, lista2, lista3):
    for x in range(10):
        if lista[x]>0:
            lista2.append(lista[x])

        elif lista[x]<0:
            lista3.append(lista[x])

    print(f"Lista originial: {lista}")
    print(f"Lista de numeros positivos: {lista2}")
    print(f"Lista de numero negativos: {lista3}")

valores=[]
ListaPos=[]
ListaNeg=[]

cargardatos(valores)
doslistas(valores, ListaPos, ListaNeg)