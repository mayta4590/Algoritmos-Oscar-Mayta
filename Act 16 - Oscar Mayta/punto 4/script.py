"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""
docentes = []
puntajes = []

for x in range(6):

    nom = input("Ingrese el nombre del docente: ")
    docentes.append(nom)

    nota = float(input("Ingrese la calificación: "))
    puntajes.append(nota)

mayor = puntajes[0]
menor = puntajes[0]

for x in range(6):

    if puntajes[x] > mayor:
        mayor = puntajes[x]

    if puntajes[x] < menor:
        menor = puntajes[x]

print("\nDocente con calificación más alta:")

for x in range(6):
    if puntajes[x] == mayor:
        print(docentes[x], "-", puntajes[x])

print("\nDocente con calificación más baja:")

for x in range(6):
    if puntajes[x] == menor:
        print(docentes[x], "-", puntajes[x])

for k in range(5):

    for x in range(5-k):

        if puntajes[x] < puntajes[x+1]:

            auxpuntaje = puntajes[x]
            puntajes[x] = puntajes[x+1]
            puntajes[x+1] = auxpuntaje

            auxdocente = docentes[x]
            docentes[x] = docentes[x+1]
            docentes[x+1] = auxdocente

print("\nDocentes ordenados por calificación:")

for x in range(6):
    print(docentes[x], "-", puntajes[x])

aprobados = 0
desaprobados = 0

for x in range(6):

    if puntajes[x] >= 6:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1

print("\nCantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)