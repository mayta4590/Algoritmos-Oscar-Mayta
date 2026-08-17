"""
Ejercicio 4: Algoritmo de Compresión de Texto (RLE)
Contexto: En telecomunicaciones se utiliza el algoritmo Run-Length Encoding (RLE) para
comprimir secuencias de caracteres repetidos y ahorrar ancho de banda.
Consigna: Escribir la función comprimir_rle(texto) que reciba una cadena de caracteres en
mayúsculas y devuelva su versión comprimida.
Requisitos:
● Contar las apariciones consecutivas de cada carácter.
● Construir una cadena resultante intercalando el carácter con su cantidad de
apariciones consecutivas.
Ejemplo de Entrada: &quot;AAABBCDDDD&quot; Salida Esperada: &quot;A3B2C1D4&quot;
"""

def comparar_caracteres(texto, i):
    return texto[i] == texto[i + 1]


def comprimir_rle(texto):

    resultado = ""
    contador = 1

    for i in range(len(texto) - 1):

        if comparar_caracteres(texto, i):
            contador = contador + 1
        else:
            resultado = resultado + texto[i] + str(contador)
            contador = 1

    resultado = resultado + texto[-1] + str(contador)

    return resultado


texto = input("Ingrese un texto: ")

print("Texto original:", texto)
print("Texto comprimido:", comprimir_rle(texto))