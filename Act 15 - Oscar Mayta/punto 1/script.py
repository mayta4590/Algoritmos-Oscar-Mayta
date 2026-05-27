"""
1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar &quot;Muy Bueno&quot; si la nota es mayor o
igual a 8, &quot;Bueno&quot; si la nota está entre 4 y 7, y colocar &quot;Insuficiente&quot;
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.
"""

alumnos = []
notas = []

for x in range(4):
    alum = input(f"Ingrese el nombre del alumno n°{x+1}: ")
    alumnos.append(alum)

    nota = int(input(f"Ingrese la nota del alumno n°{x+1}: "))
    notas.append(nota)

muy_bueno = 0

print("\nListado de alumnos:")

for x in range(4):

    if notas[x] >= 8:
        condicion = "Muy Bueno"
        muy_bueno = muy_bueno + 1

    elif notas[x] >= 4:
        condicion = "Bueno"

    else:
        condicion = "Insuficiente"

    print(f"Alumno: {alumnos[x]} - Nota: {notas[x]} - Condición: {condicion}")

print(f"\nCantidad de alumnos con 'Muy Bueno': {muy_bueno}")