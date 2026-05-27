"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.
"""

lista1 = []
lista2 = []
lista3 = []

print("Carga de la primera lista")
for x in range(4):
    num = int(input(f"Ingrese un número para la posición {x+1}: "))
    lista1.append(num)

print("\nCarga de la segunda lista")
for x in range(4):
    num = int(input(f"Ingrese un número para la posición {x+1}: "))
    lista2.append(num)

for x in range(4):
    suma = lista1[x] + lista2[x]
    lista3.append(suma)

print("\nPrimera lista:", lista1)
print("Segunda lista:", lista2)
print("Tercera lista (sumas):", lista3)