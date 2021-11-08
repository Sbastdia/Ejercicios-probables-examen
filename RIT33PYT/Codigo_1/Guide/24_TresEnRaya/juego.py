import sys

from itertools import cycle

from introducir import (
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
)


JUGADORES = ["X", "O"]


def jugar_tirada(tabla, jugador):
    """Permite gestionar el dato introducido de una tirada"""
    while True:
        linea = solicitar_introducir_numero_extremo(
            "Jugador {}, seleccione la línea".format(jugador), 1, 3) - 1
        columna = solicitar_introducir_numero_extremo(
            "Jugador {}, seleccione la columna".format(jugador), 1, 3) - 1

        if tabla[linea][columna] != " ":
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        else:
            tabla[linea][columna] = jugador
            return tabla


TRAZO_HORIZONTAL = " " + "+---" * 3 + "+"

def ver_tabla(tabla):
    for linea in tabla:
        print(TRAZO_HORIZONTAL)
        for casilla in linea:
            print(" |", casilla, end="")
        print(" |")
    print(TRAZO_HORIZONTAL + "\n\n")


def probar_fin_juego(tabla):
    """Permite probar si el juego ha terminado o no"""
    if tabla[0][0] != " ":
        return True


def jugar_una_partida():
    """Algoritmo de una partida"""
    # Creamos un tablero de juego vacío
    tabla = [[" "] * 3] * 3
    # >>> a=[[""] * 3] * 3
    # >>> a[0] is a[1]
    # True


    for jugador in cycle(JUGADORES):
        ver_tabla(tabla)

        # Turno a turno, cada jugador juega
        tabla = jugar_tirada(tabla, jugador)

        if probar_fin_juego(tabla):
            # Si el juego ha terminado, salimos de la función
            ver_tabla(tabla)
            return



def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? ? [s/n]")


def jugar():
    while True:
        jugar_una_partida()

        if not elegir_jugarOtra():
            return

