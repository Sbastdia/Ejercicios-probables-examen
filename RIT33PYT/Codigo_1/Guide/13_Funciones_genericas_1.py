"""
Ejercicio: hacer un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Adivinar el número por parte del usuario

Usar una función para capitalizar el código común
"""

MIN = 0
MAX = 99


def solicitar_introducir_numero(invite):
    # Completar la entrada:
    invite += " entre " + str(MIN) + " y " + str(MAX) + " incluídos: "

    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = input(invite)

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            pass
        else:
            # Hacer la comparación
            if MIN <= datoIntroducido <= MAX:
                # Tenemos lo que queremos, salimos del bucle
                break
    return datoIntroducido


# PARTE 1
numero = solicitar_introducir_numero("Introduzca el número a adivinar")


# PARTE 2
while True:
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    intento = solicitar_introducir_numero("Adivine el número")

    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Victoria!")
        break

