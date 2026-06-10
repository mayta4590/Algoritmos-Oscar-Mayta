"""2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado."""

def Articulos_Precios(nom, pre):

    for x in range(5):
        valor1= input(f"Ingrese el nombre del articulo n°{x+1}: ")
        nom.append(valor1)
        valor2=int(input(f"Ingrese el precio de {nom[x]}: "))
        pre.append(valor2)
    return nom , pre 


def precioMayor(li):
    mayor=0
    for x in range(5):
        if li[x] > mayor:
            mayor= li[x]
            nomM= nombres[x]
    return nomM


def importe(lu):
    nomm=[]
    imp=int(input("Ingrese un importe: "))
    for x in range(5):
        if lu[x] < imp:
            imp=lu[x]
            nomm.append(nombres[x])
    return nomm

nombres=[]
precios=[]

lista=Articulos_Precios(nombres, precios)
print(lista)
alto=precioMayor(precios)
print(f"El precio mayor es: {alto}")
bajo= importe(precios)
print(f"Precios menores: {bajo} ")