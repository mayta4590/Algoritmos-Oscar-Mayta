"""
3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio.
"""
nombres = []
tiempos = []

for x in range(5):

    nom = input("Ingrese el nombre del atleta: ")
    nombres.append(nom)

    tiempo = float(input("Ingrese el tiempo en segundos: "))
    tiempos.append(tiempo)

suma = 0

for x in range(5):
    suma = suma + tiempos[x]

promedio = suma / 5

print("\nEl promedio de los tiempos es:", promedio)

mejor = tiempos[0]
peor = tiempos[0]

for x in range(5):

    if tiempos[x] < mejor:
        mejor = tiempos[x]

    if tiempos[x] > peor:
        peor = tiempos[x]

print("\nAtleta con mejor tiempo:")

for x in range(5):
    if tiempos[x] == mejor:
        print(nombres[x], "-", tiempos[x])

print("\nAtleta con peor tiempo:")

for x in range(5):
    if tiempos[x] == peor:
        print(nombres[x], "-", tiempos[x])

print("\nAtletas que superaron el promedio:")

for x in range(5):
    if tiempos[x] < promedio:
        print(nombres[x], "-", tiempos[x])