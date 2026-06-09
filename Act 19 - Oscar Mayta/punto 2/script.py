"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def cargarDatos():
    for x in range(10):
        valor=int(input(f"Ingrese el sueldo de la persona n°{x+1}: "))
        sueldos.append(valor)
    
    print("lista completa: ", sueldos)
    
    for x in range(10):
        print(sueldos[x])

def sueldo4000():
    cont4000=0
    for x in range(10):
        if sueldos[x]>4000:
            cont4000=cont4000+1
    
    print("Cantidad de sueldo mayor a 4000 son: ", cont4000)

def promedio_debajoprom():
    promedio=0
    prom=0
    for x in range(10):
        promedio=promedio + sueldos[x]
        prom=promedio/10

    print("El promedo de todos los sueldos es: ", prom)

    for x in range(10):
        if sueldos[x]<prom:
            lista2.append(sueldos[x])
            print("Los sueldos debajo del promedio son: ", lista2[x])



        
    
lista2=[]
sueldos=[]

cargarDatos()
sueldo4000()
promedio_debajoprom()