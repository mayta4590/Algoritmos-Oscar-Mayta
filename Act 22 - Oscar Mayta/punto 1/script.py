"""
1-
Crear un diccionario en Python que defina como clave el número de documento de
una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""

def cargar():
    personas = {}
    for i in range(4):
        dni = int(input("Ingrese el número de documento: "))
        nombre = input("Ingrese el nombre: ")
        personas[dni] = nombre
    return personas

def imprimir(personas):
    print("Listado completo:")
    for dni in personas:
        print(dni, personas[dni])

def consulta(personas):
    dni = int(input("Ingrese el número de documento a consultar: "))
    if dni in personas:
        print("Nombre:", personas[dni])
    else:
        print("No existe una persona con ese documento.")

personas = cargar()
imprimir(personas)
consulta(personas)