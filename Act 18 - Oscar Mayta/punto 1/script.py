"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""

def menor(v1, v2, v3):
    if v1 < v2 and v1 < v3:
        return v1
    elif v2 < v3:
        return v2
    else:
        return v3

def solicitar_mostrar():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    print("El menor es:", menor(valor1, valor2, valor3))

solicitar_mostrar()
solicitar_mostrar()