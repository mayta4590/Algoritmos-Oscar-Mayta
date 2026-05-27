"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""

paises = []
habitantes = []

for x in range(5):

    pais = input(f"Ingrese el nombre del país n°{x+1}: ")
    paises.append(pais)

    hab = int(input(f"Ingrese la cantidad de habitantes de {pais}: "))
    habitantes.append(hab)

for k in range(4):

    for x in range(4-k):

        if paises[x] > paises[x+1]:

            auxpais = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = auxpais

            auxhab = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = auxhab

print("\nPaíses ordenados alfabéticamente:")

for x in range(5):
    print(paises[x], "-", habitantes[x])

for k in range(4):

    for x in range(4-k):

        if habitantes[x] < habitantes[x+1]:

            auxhab = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = auxhab

            auxpais = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = auxpais

print("\nPaíses ordenados por cantidad de habitantes:")

for x in range(5):
    print(paises[x], "-", habitantes[x])