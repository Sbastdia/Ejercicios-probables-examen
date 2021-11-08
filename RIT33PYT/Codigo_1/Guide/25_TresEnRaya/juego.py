import sys

from itertools import cycle, chain

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
        print("|")
    print(TRAZO_HORIZONTAL + "\n\n")


def probar_fin_juego(tabla):
    """Permite probar si el juego ha terminado o no"""

    # Probar las líneas
    for linea in tabla:
        if línea[0] == línea[1] == línea[2] != " ":
            print("El jugador {} ha ganado".format(linea[0]))
            return True

    # Probar las columnas
    for columna in zip(*tabla):
        if columna[0] == columna[1] == columna[2] != " ":
            print("El jugador {} ha ganado".format(columna[0]))
            return True

    # Probar las diagonales
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != " " or\
       tabla[2][0] == tabla[1][1] == tabla[0][2] != " ":
        print("El jugador {} ha ganado".format(tabla[1][1]))
        return True

    # Probar que todavía quedan turnos por jugar
    for casilla in chain(*tabla):
        if casilla == " ":
            return False
    else:
        print("El juego se ha terminado en empate!")
        return True


def jugar_una_partida():
    """Algoritmo de una partida"""
    # Creamos un tablero de juego vacío
    tabla = [[" "] * 3 for _ in range(3)]
    # >>> a=[[""] * 3] for _ in range(3)]
    # >>> a[0] is a[1]
    # False

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

