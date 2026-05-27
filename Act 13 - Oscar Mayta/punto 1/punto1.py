#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
# Además el programa deberá informar el importe que gasta la empresa en sueldos

n = int(input("Ingrese la cantidad de empleados: "))

entre_100_300 = 0
mas_300 = 0
total_sueldos = 0

for i in range(n):
    sueldo = float(input(f"Ingrese el sueldo del empleado n°{i+1}: "))
    
    if sueldo>=100 and sueldo <=300:
        entre_100_300 = entre_100_300 + 1
    elif sueldo > 300:
        mas_300 = mas_300 + 1
    
    total_sueldos = total_sueldos + sueldo

print("\nResultados:")
print("Empleados que cobran entre $100 y $300:", entre_100_300)
print("Empleados que cobran más de $300:", mas_300)
print("Importe total que gasta la empresa en sueldos:", total_sueldos)