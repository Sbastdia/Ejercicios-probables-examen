import sys

from itertools import cycle, chain, product
from random import shuffle

from introducir import (
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
)


TAMANIOS = [(2, 3), (4, 4), (4, 4), (4, 6), (4, 6)]
ORDINALES = [0x2600, 0x2654, 0x263D, 0x2654, 0x2648]


CARTA_A_ENCONTRAR = chr(0x2610)


def jugar_tirada(tamanio, diccionario, letras_encontradas):
    """Permite gestionar el dato introducido de una tirada"""
    while True:
        linea1 = solicitar_introducir_numero_extremo(
            "línea de la primera carta", 1, tamanio[0]) - 1
        columna1 = solicitar_introducir_numero_extremo(
            "columna de la primera carta", 1, tamanio[1]) - 1
        if diccionario[linea1, columna1] in letras_encontradas:
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        else:
            break
    print("La primera casilla es {}".format(diccionario[linea1, columna1]))

    while True:
        linea2 = solicitar_introducir_numero_extremo(
            "línea de la segunda carta", 1, tamanio[0]) - 1
        columna2 = solicitar_introducir_numero_extremo(
            "columna de la segunda carta", 1, tamanio[1]) - 1
        if diccionario[linea2, columna2] in letras_encontradas:
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        elif linea1 == linea2 and columna1 == columna2:
            print("Ha seleccionado dos veces la misma casilla, por favor, cámbiela",
                file=sys.stderr)
        else:
            break
    print("La segunda casilla es {}".format(diccionario[linea2, columna2]))

    if diccionario[linea1, columna1] == diccionario[linea2, columna2]:
        print("Acaba de encontrar dos cartas iguales.")
        return diccionario[linea1, columna1]
    print("No ha encontrado una carta nueva.")


def ver_tabla(tamanio, diccionario, letras_encontradas):
    trazo_horizontal = " " + "+---" * tamanio[1] + "+"
    for (x, y) in product(range(tamanio[0]), range(tamanio[1])):
        # Trazo horizontal para cada nueva línea
        if y == 0:
            print(trazo_horizontal)

        # Encontrar la casilla correcta
        casilla = diccionario[x, y]

        # Ocultar temporalmente, después ver la casilla, como antes
        if casilla not in letras_encontradas:
            casilla = CARTA_A_ENCONTRAR
        print(" |", casilla, end="")

        # Ver la barra vertical derecha del tablero:
        if y == tamanio[1] - 1:
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
    lista = list(product(range(tamanio[0]), range(tamanio[1])))
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

