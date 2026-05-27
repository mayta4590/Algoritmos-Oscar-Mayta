"""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""

empleados=[]
faltas=[]

for x in range(3):
    nombre=input(f"Ingrese el nombre del empleado N°{x+1}: ")
    empleados.append(nombre)
    cantidad=int(input(f"¿Cuantos dias falto {nombre}?: "))
    faltas.append([])

    for k in range(cantidad):
        dia=int(input("Ingrese el día que faltó: "))
        faltas[x].append(dia)

print("Listado de empleados y faltas")

for x in range(3):
    print("Empleado:", empleados[x])

    for k in range(len(faltas[x])):
        print("Faltó el día:", faltas[x][k])

print("Cantidad de inasistencias")

for x in range(3):
    print(empleados[x], "falto", len(faltas[x]), "días")

menor=len(faltas[0])

for x in range(1,3):
    if len(faltas[x]) < menor:
        menor=len(faltas[x])

print("Empleados con menos inasistencias")
for x in range(3):
    if len(faltas[x]) == menor:
        print(empleados[x])