#5. Realizar un programa que lea los lados de n triángulos, e informar:
#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.

n = int(input("Ingrese la cantidad de triángulos: "))

equilateros = 0
isoceles = 0
escalenos = 0

for i in range(n):
    print(f"\nTriángulo {i+1}:")
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))
    
    if a == b == c:
        print("Es un triángulo equilátero")
        equilateros += 1
    elif a == b or a == c or b == c:
        print("Es un triángulo isósceles")
        isoceles += 1
    else:
        print("Es un triángulo escaleno")
        escalenos += 1

print("\nResumen:")
print("Equiláteros:", equilateros)
print("Isósceles:", isoceles)
print("Escalenos:", escalenos)