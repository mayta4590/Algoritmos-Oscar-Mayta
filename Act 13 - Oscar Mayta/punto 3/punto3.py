#3. Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") 
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

suma1 = 0
suma2 = 0

print("Carga de la lista 1:")
for i in range(15):
    valor = int(input(f"Ingrese valor {i+1}: "))
    suma1 = suma1 + valor

print("\nCarga de la lista 2:")
for i in range(15):
    valor = int(input(f"Ingrese valor {i+1}: "))
    suma2 = suma2 + valor

if suma1 > suma2:
    print("\nLista 1 mayor")
elif suma2 > suma1:
    print("\nLista 2 mayor")
else:
    print("\nListas iguales")