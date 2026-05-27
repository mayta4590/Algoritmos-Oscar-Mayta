"""
4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""

empleados=[]
sueldos=[]

cantidad=int(input("Ingrese la cantidad de empleados: "))

for x in range(cantidad):
    nombre=input(f"Ingrese el nombre del empleado N°{x+1}: ")
    empleados.append(nombre)

    sueldo=float(input(f"Ingrese el sueldo de {nombre}: "))
    sueldos.append(sueldo)

print("Lista original de empleados")

for x in range(len(empleados)):
    print(empleados[x], ":", sueldos[x])

posicion=0

while posicion < len(sueldos):
    if sueldos[posicion] > 10000:
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion=posicion+1

print("Empleados con sueldo menor o igual a 10000")

for x in range(len(empleados)):
    print(empleados[x], ":", sueldos[x])