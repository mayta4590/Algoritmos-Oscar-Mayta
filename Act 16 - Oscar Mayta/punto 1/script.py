"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""
nombres = []
notas = []

for x in range(6):
    nom = input("Ingrese el nombre del estudiante: ")
    nombres.append(nom)

    nota = float(input("Ingrese la nota: "))
    notas.append(nota)

mayor = notas[0]
menor = notas[0]

for x in range(6):
    if notas[x] > mayor:
        mayor = notas[x]

    if notas[x] < menor:
        menor = notas[x]

print("\nNota más alta:")

repetido_mayor = 0

for x in range(6):
    if notas[x] == mayor:
        print(nombres[x], mayor)
        repetido_mayor = repetido_mayor + 1

print("\nNota más baja:")

repetido_menor = 0

for x in range(6):
    if notas[x] == menor:
        print(nombres[x], menor)
        repetido_menor = repetido_menor + 1

if repetido_mayor > 1:
    print("\nHay estudiantes con la misma nota máxima.")

if repetido_menor > 1:
    print("Hay estudiantes con la misma nota mínima.")