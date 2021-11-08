"""
Introducción a los Bloques iterativos.

El bucle infinito debe terminar en algún momento.
En este ejemplo, el bucle se ejecuta al menos una vez obligatoriamente.
"""


while True:
    # Entramos en un bucle infinito

    # Pedimos introducir un número
    numero = input("Introduzca un número entre 1 y 10: ")

    try:
        numero = int(numero)
    except:
        pass
    else:
        # Hacer la comparación
        if 1 <= numero <= 10:
            # Tenemos lo que queremos, salimos del bucle
            break

print("Estamos seguros de que", numero, "es un número y que está comprendido entre 1 y 10 incluídos")

