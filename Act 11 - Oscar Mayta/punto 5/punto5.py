#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

num=int(input("Ingresar un valor entero: "))

if num>0:
    print("El numero es positivo")
else:
    if num<0:
        print("El numero negativo")
    else:
        print("El numero es nulo")