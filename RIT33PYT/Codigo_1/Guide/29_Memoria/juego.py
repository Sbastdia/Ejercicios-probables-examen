import sys

from itertools import cycle, chain, product
from random import shuffle

from introducir import (
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
    solicitar_introducir_casilla,
)


TAMANIOS = [(2, 3), (4, 4), (4, 4), (4, 6), (4, 6)]
ORDINALES = [0x2600, 0x2654, 0x263D, 0x2654, 0x2648]


CARTA_A_ENCONTRAR = chr(0x2610)


def jugar_tirada(tamanio, diccionario, letras_encontradas):
    """Permite gestionar el dato introducido de una tirada"""
    while True:
        casilla1 = solicitar_introducir_casilla(
            "Seleccionar una primera casilla (letra + cifra)")
        if diccionario[casilla1] in letras_encontradas:
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        else:
            break
    print("La primera casilla es {}".format(diccionario[casilla1]))

    while True:
        casilla2 = solicitar_introducir_casilla(
            "Seleccionar una segunda casilla (letra + cifra)")
        if diccionario[casilla2] in letras_encontradas:
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        elif casilla1 == casilla2:
            print("Ha seleccionado dos veces la misma casilla, por favor, cámbiela",
                file=sys.stderr)
        else:
            break
    print("La segunda casilla es {}".format(diccionario[casilla2]))

    if diccionario[casilla1] == diccionario[casilla2]:
        print("Acaba de encontrar dos cartas iguales.")
        return diccionario[casilla1]
    print("No ha encontrado una carta nueva.")


def ver_tabla(tamanio, diccionario, letras_encontradas):
    letras = [chr(x) for x in range(65, 65 + tamanio[0])]
    cifras = [str(x) for x in range(tamanio[1])]

    trazo_horizontal = " --" + "+---" * tamanio[1] + "+"

    print("   |", " | ".join(cifras), "|")

    iter_letras = iter(letras)

    for coordenada in ["".join(x) for x in product(letras, cifras)]:
        # Trazo horizontal para cada nueva línea
        if coordenada[1] == "0":
            print(trazo_horizontal)
            print(" {}".format(next(iter_letras)), end="")

        # Encontrar la casilla correcta
        diccionario[coordenada]

        # Ocultar temporalmente, después ver la casilla, como antes
        if casilla not in letras_encontradas:
            casilla = CARTA_A_ENCONTRAR
        print(" |", casilla, end="")

        # Ver la barra vertical derecha del tablero:
        if coordenada[1] == str(tamanio[1] - 1):
            print(" |")
    # Ver la última línea horizontal
    print(trazo_horizontal + "\n\n")


def probar_fin_juego(tamanio, letras_encontradas):
    """Permite probar si el juego ha terminado o no"""
    if len(letras_encontradas) >= int(tamanio[0] * tamanio[1] / 2):
        print("Bravo. El juego ha terminado !")
        return True

    return False


def crear_diccionario(tamanio, ordinal):
    letras = [chr(x) for x in range(65, 65 + tamanio[0])]
    cifras = [str(x) for x in range(tamanio[1])]
    lista = ["".join(x) for x in product(letras, cifras)]
    shuffle(lista)
    diccionario = {}
    for index, coordenada in enumerate(lista):
        diccionario[coordenada] = chr(ordinal)
        if index % 2 == 1:
            ordinal += 1
    return diccionario


def jugar_una_partida(tamanio, ordinal):
    """Algoritmo de una partida"""
    # Creamos un tablero de juego vacío
    diccionario = crear_diccionario(tamanio, ordinal)

    letras_encontradas = []

    while True:
        ver_tabla(tamanio, diccionario, letras_encontradas)

        letra = jugar_tirada(tamanio, diccionario, letras_encontradas)
        if letra is not None:
            letras_encontradas.append(letra)

        if probar_fin_juego(tamanio, letras_encontradas):
            # Si el juego ha terminado, salimos de la función
            ver_tabla(tamanio, diccionario, letras_encontradas)
            return


def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? ? [s/n]")


def elegir_nivel():
    return solicitar_introducir_numero_extremo(
            "¿Qué nivel desea?", 1, len(TAMANIOS)) - 1


def jugar():
    while True:
        nivel = elegir_nivel()

        tamanio = TAMANIOS[nivel]
        ordinal = ORDINALES[nivel]

        jugar_una_partida(tamanio, ordinal)

        if not elegir_jugarOtra():
            return

