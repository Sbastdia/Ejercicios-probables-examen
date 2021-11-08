"""
Ejercicio: hacer un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Adivinar el número por parte del usuario

Usar una función para capitalizar el código común
"""

def solicitar_introducir_numero():
    while True:
        # Entramos en un bucle infinito
        # que permite corregir una error de escritura

        # Pedimos introducir un número
        datoIntroducido = input("Introduzca un número entre 0 y 99 incluídos: ")

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            pass
        else:
            # Hacer la comparación
            if 9 <= datoIntroducido <= 99:
                # Tenemos lo que queremos, salimos del bucle
                break
    return datoIntroducido


# PARTE 1
print("Introduzca el número a adivinar")
numero = solicitar_introducir_numero()


# PARTE 2
print("intente encontrar el número a adivinar")
while True:
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    intento = solicitar_introducir_numero()

    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print ("Victoria!")
        break

