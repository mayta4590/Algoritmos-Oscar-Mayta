# 6. De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
#a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
#c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

sueldo=int(input("Ingresar el sueldo del operario: "))
añosantiguedad=int(input("Ingresar los años de antiguedad del operario: "))

if sueldo<500 and añosantiguedad>=10:
    aumento=sueldo*20/100
    sueldofinal=sueldo+aumento
    print("El sueldo a pagar es: ")
    print(sueldofinal)

else:
    if sueldo<500 and añosantiguedad<10:
        aumento=sueldo*5/100
        sueldofinal=sueldo+aumento
        print("El sueldo a pagar es: ")
        print(sueldofinal)

    else:
        print("El sueldo a pagar es: ")
        print(sueldo)

