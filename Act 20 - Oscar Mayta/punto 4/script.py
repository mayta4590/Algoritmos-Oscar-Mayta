"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""

def recibir(edad):
    cont = 0
    for x in range(len(edad)):
        if edad[x] >= 18:
            cont = cont + 1
    return cont

edades = [6, 32, 2, 19, 25, 9]
cantidad = recibir(edades)
print(f"Hay {cantidad} mayores o igual a 18")
