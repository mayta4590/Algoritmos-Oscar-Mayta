#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores

mayor = 0
menor = 0

for f in range(10):
    nota=int(input("Ingrese las notas de los alumnos "))  
    if nota>=7:
        mayor=mayor+1
    else:
        menor=menor+1
        
        
print("Las notas mayor o igual a 7 son: ")
print(mayor)
print("Las notas menores a 7 son: ")
print(menor)