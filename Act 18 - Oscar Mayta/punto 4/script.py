"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A".
"""

def cantidad_a(cadena):
    cant = 0
    for x in cadena:
        if x == "a" or x == "A":
            cant = cant + 1
    return cant

texto = input("Ingrese un texto: ")
cantidad = cantidad_a(texto)
print("Cantidad de letras a o A:", cantidad)