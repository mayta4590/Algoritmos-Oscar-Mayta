"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
"""

lista = []

for x in range(5):

    num = int(input(f"Ingrese el elemento n°{x+1}: "))
    lista.append(num)

for k in range(4):

    for x in range(4-k):

        if lista[x] > lista[x+1]:

            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux

print("\nLista ordenada de menor a mayor:")

for x in range(5):
    print(lista[x])

for k in range(4):

    for x in range(4-k):

        if lista[x] < lista[x+1]:

            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux
            
print("\nLista ordenada de mayor a menor:")

for x in range(5):
    print(lista[x])