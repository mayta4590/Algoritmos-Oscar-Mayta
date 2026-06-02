"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""

def retornar_superficie(lado1, lado2):
    sup = lado1 * lado2
    return sup

l1 = int(input("Ingrese el lado 1 del rectángulo 1: "))
l2 = int(input("Ingrese el lado 2 del rectángulo 1: "))

l3 = int(input("Ingrese el lado 1 del rectángulo 2: "))
l4 = int(input("Ingrese el lado 2 del rectángulo 2: "))

sup1 = retornar_superficie(l1, l2)
sup2 = retornar_superficie(l3, l4)

if sup1 > sup2:
    print("El rectángulo 1 tiene mayor superficie")
elif sup2 > sup1:
    print("El rectángulo 2 tiene mayor superficie")
else:
    print("Ambos tienen la misma superficie")