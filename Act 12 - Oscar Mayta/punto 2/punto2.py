#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

suma=0

n=int(input("Cuantas personas se van a medir: "))
for f in range(n):
    altura=int(input("Ingrese la altura de la persona: "))
    suma=suma+altura

promedio=suma/n
print("El promedio es: ")
print(promedio)