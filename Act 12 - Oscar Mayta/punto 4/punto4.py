#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multiplos15 = 0
suma_pares = 0

for f in range(10):
    valor=int(input("Ingrese un valor: "))  
    if valor < 0:
        negativos = negativos + 1
    elif valor > 0:
        positivos = positivos + 1

    if valor % 15 == 0:
        multiplos15 = multiplos15 + 1

    if valor % 2 == 0:
        suma_pares = suma_pares + valor

print("La cantidad de valores ingresados negativos son: ")
print(negativos)
print("La cantidad de valores ingresados positivos son: ")
print(positivos)
print("La cantidad de múltiplos de 15 son: ")
print(multiplos15)
print("La suma de números pares son: ")
print(suma_pares)