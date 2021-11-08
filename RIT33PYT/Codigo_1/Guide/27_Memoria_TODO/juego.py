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
        # TODO: solicitar el ataque de las coordenadas, es decir, de la línea y columna
        # Se inspirar en el juego de tres en raya
        linea1 = 1
        columna1 = 1
        # TODO: Si la carta ya ha sido encontrada, empezamos de nuevo el proceso de pedir un dato.
        # TODO: En caso contrario, salimos del bucle infinito
    print("La primera casilla es {}".format(tabla[linea1][columna1]))

    while True:
        # TODO: A continuación, se solicita el ataque de una segunda casilla
        linea2 = 1
        columna2 = 2
        # TODO: Si la carta ya ha sido encontrada, empezamos de nuevo el proceso de pedir un dato 2.
        # TODO: Si la carta 2 es la misma que la carta 1, empezamos de nuevo 2.
        # TODO: En caso contrario, salimos del bucle infinito
    print("La segunda casilla es {}".format(tabla[linea2][columna2]))

    # Si los dos casillas son idénticas, hemos encontrado una carta
    if tabla[linea1][columna1] == tabla[linea2][columna2]:
        print("Acaba de encontrar dos cartas iguales.")
        return tabla[linea1][columna1]
    # En caso contrario, no hemos encontrado carta, permanecen ocultas.
    print("No ha encontrado una carta nueva.")


def ver_tabla(tamanio, tabla, cartas_encontradas):
    trazo_horizontal = " " + "+---" * tamanio[1] + "+"
    for linea in tabla:
        print(trazo_horizontal)
        for casilla in línea:
            if casilla not in cartas_encontradas:
                casilla = CARTA_A_ENCONTRAR
            print(" |", casilla, end="")
        print(" |")
    print(trazo_horizontal + "\n\n")


def probar_fin_juego(tamanio, cartas_encontradas):
    """Permite probar si el juego ha terminado o no"""
    # TODO: Si todas los cartas son devueltas, se gana el juego
    return False


def crear_tabla(tamanio, ordinal):
    # TODO: Crear un tabla que contiene dos veces cada carta (y mezcladas)
    return False


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

