#7. Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    mayor = num1
else:
    if num2 > num1 and num2 > num3:
        mayor = num2
    else:
        mayor = num3

if num1 < num2 and num1 < num3:
    menor = num1
else:
    if num2 < num1 and num2 < num3:
        menor = num2
    else:
        menor = num3

print("El número mayor es:")
print(mayor)

print("El número menor es:")
print(menor)