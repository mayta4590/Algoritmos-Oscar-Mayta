#2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada cuenta corriente se conoce: número de cuenta y saldo actual. 
# El ingreso de datos debe finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un programa que lea los datos de las cuentas corrientes e informe:
#● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo, sabiendo que:
#○ Estado de la cuenta:
#○ “Acreedor” si el saldo es > 0.
#○ “Deudor” si el saldo es < 0.
#○ “Nulo” si el saldo es = 0.
#● b) La suma total de los saldos acreedores.

suma_acreedores = 0

numero_cuenta = int(input("Ingrese numero de cuenta: "))

while numero_cuenta >= 0:
    saldo = float(input("Ingrese el saldo de la cuenta: "))
    
    if saldo > 0:
        print("Cuenta", numero_cuenta, "- Estado: Acreedor")
        suma_acreedores = suma_acreedores + saldo
    elif saldo < 0:
        print("Cuenta", numero_cuenta, "- Estado: Deudor")
    else:
        print("Cuenta", numero_cuenta, "- Estado: Nulo")
    
    numero_cuenta = int(input("Ingrese numero de cuenta: "))

print("\nSuma total de saldos acreedores:", suma_acreedores)