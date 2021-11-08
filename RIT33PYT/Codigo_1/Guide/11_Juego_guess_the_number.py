"""
Ejercicio: hacer un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Adivinar el número por parte del usuario

"""

# PARTE 1

# Para el ejercicio del primer capítulo, hay que utilizar lo que sigue:
# import random
# numero = random.randint(0, 100)

# Para resaltar el segundo capítulo, hay que utilizar lo que sigue:
print("Introduzca el número a adivinar")
while True:
    # Entramos en un bucle infinito

    # Pedimos introducir un número
    numero = input("Introduzca un número entre 0 y 99 incluídos: ")

    try:
        numero = int(numero)
    except:
        pass
    else:
        # Hacer la comparación
        if 0 <= numero <= 99:
            # Tenemos lo que queremos, salimos del bucle
            break

# PARTE 2
print("intente encontrar el número a adivinar")
while True:  # BUCLE 1
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    while True:  # BUCLE 2
        # Entramos en un bucle infinito
        # que permite corregir un error de escritura

        # Pedimos introducir un número
        intento = input("Introduzca un número entre 0 y 99 incluídos: ")

        try:
            intento = int(intento)
        except:
            pass
        else:
            # Hacer la comparación
            if 0 <= intento <= 99:
                # Tenemos lo que queremos, salimos del BUCLE 2
                break

    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Victoria!")
        # Terminamos la partida, salimos del BUCLE 1
        break

