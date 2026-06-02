"""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""

def ordenados(n1, n2, n3):
    if n1 > n2:
        n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n2 > n3:
        n2, n3 = n3, n2

    print("Ordenados de menor a mayor: ")
    print(n1,"-", n2,"-", n3)


def solicitar():
    numero1=int(input("Ingrese el primer valor: "))
    numero2=int(input("Ingrese el segundo valor: "))
    numero3=int(input("Ingrese el tercer valor: "))
    ordenados(numero1,numero2,numero3)

solicitar()