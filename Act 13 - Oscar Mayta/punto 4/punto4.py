#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. 
# #Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. 
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

primer_cuadrante = 0
segundo_cuadrante = 0
tercer_cuadrante = 0
cuarto_cuadrante = 0

n = int(input("Ingrese la cantidad de puntos: "))

for i in range(n):
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        primer_cuadrante = primer_cuadrante + 1

    elif x < 0 and y > 0:
        segundo_cuadrante = segundo_cuadrante + 1

    elif x < 0 and y < 0:
        tercer_cuadrante = tercer_cuadrante + 1

    elif x > 0 and y < 0:
        cuarto_cuadrante = cuarto_cuadrante + 1

print("\nCantidad de puntos en el primer cuadrante:", primer_cuadrante)
print("Cantidad de puntos en el segundo cuadrante:", segundo_cuadrante)
print("Cantidad de puntos en el tercer cuadrante:", tercer_cuadrante)
print("Cantidad de puntos en el cuarto cuadrante:", cuarto_cuadrante)