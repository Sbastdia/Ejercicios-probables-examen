import sys

from itertools import cycle, chain
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


def jugar_tirada(tamanio, tabla, cartas_encontradas):
    """Permite gestionar el dato introducido de una tirada"""
    while True:
        linea1 = solicitar_introducir_numero_extremo(
            "línea de la primera carta", 1, tamanio[0]) - 1
        columna1 = solicitar_introducir_numero_extremo(
            "columna de la primera carta", 1, tamanio[1]) - 1
        if tabla[linea1][columna1] in cartas_encontradas:
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        else:
            break
    print("La primera casilla es {}".format(tabla[linea1][columna1]))

    while True:
        linea2 = solicitar_introducir_numero_extremo(
            "línea de la segunda carta", 1, tamanio[0]) - 1
        columna2 = solicitar_introducir_numero_extremo(
            "columna de la segunda carta", 1, tamanio[1]) - 1
        if tabla[linea2][columna2] in cartas_encontradas:
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        elif linea1 == linea2 and columna1 == columna2:
            print("Ha seleccionado dos veces la misma casilla, por favor, cámbiela",
                file=sys.stderr)
        else:
            break
    print("La segunda casilla es {}".format(tabla[linea2][columna2]))

    if tabla[linea1][columna1] == tabla[linea2][columna2]:
        print("Acaba de encontrar dos cartas iguales.")
        return tabla[linea1][columna1]
    print("No ha encontrado una carta nueva.")


def ver_tabla(tamanio, tabla, cartas_encontradas):
    trazo_horizontal = " " + "+---" * tamanio[1] + "+"
    for linea in tabla:
        print(trazo_horizontal)
        for casilla in linea:
            if casilla not in cartas_encontradas:
                casilla = CARTA_A_ENCONTRAR
            print(" |", casilla, end="")
        print(" |")
    print(trazo_horizontal + "\n\n")


def probar_fin_juego(tamanio, cartas_encontradas):
    """Permite probar si el juego ha terminado o no"""
    if len(cartas_encontradas) >= int(tamanio[0] * tamanio[1] / 2):
        print("Bravo. El juego ha terminado !")
        return True

    return False


def crear_tabla(tamanio, ordinal):
    x, y = tamanio
    lista = [chr(x) for x in range(ordinal, ordinal + int(x * y / 2))] * 2
    shuffle(lista)
    return [liste[y*n:y*n+y] for n in range(x)]


def jugar_una_partida(tamanio, ordinal):
    """Algoritmo de una partida"""
    # Creamos un tablero de juego vacío
    tabla = crear_tabla(tamanio, ordinal)

    cartas_encontradas = []

    while True:
        ver_tabla(tamanio, tabla, cartas_encontradas)

        carta = jugar_tirada(tamanio, tabla, cartas_encontradas)
        if carta is not None:
            cartas_encontradas.append(carta)

        if probar_fin_juego(tamanio, cartas_encontradas):
            # Si el juego ha terminado, salimos de la función
            ver_tabla(tamanio, tabla, cartas_encontradas)
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

