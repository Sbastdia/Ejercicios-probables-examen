import sys

from itertools import cycle, chain, product, repeat
from functools import reduce
from random import shuffle, choice, random

from introducir import (
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
    solicitar_introducir_casilla,
)


LONGITUDES_BARCOS = [2, 3, 3, 4, 4, 5]
ORDINAL = 0x2680

CASO_NO_JUGADO = chr(0x2610)
CASO_TOCADO = chr(0x2611)
CASO_AGUA = chr(0x2612)


def jugar_tirada(casillas_jugadas):
    """Permite gestionar el dato introducido de una tirada"""
    while True:
        casilla = solicitar_introducir_casilla(
            "Seleccionar una casilla (letra + cifra)")
        if casilla in casillas_jugadas:
            print("Esta casilla ya ha sido jugada, elija otra",
                file=sys.stderr)
        else:
            return casilla


def ver_tabla(letras, cifras, casillas, barcos,
                     casillas_ocupadas, casillas_jugadas):

    trazo_horizontal = " --" + "+---" * 10 + "+"

    print("   |", " | ".join(cifras), "|")

    iter_letras = iter(letras)

    for coordenada in casillas:
        # Trazo horizontal para cada nueva línea
        if coordenada[1] == "0":
            print(trazo_horizontal)
            print(" {}".format(next(iter_letras)), end="")

        # Encontrar la casilla correcta
        if coordenada not in casillas_jugadas:
            casilla = CASO_NO_JUGADO
        elif coordenada in casillas_ocupadas:
            casilla = CASO_TOCADO
        else:
            casilla = CASO_AGUA

        print(" |", casilla, end="")

        # Ver la barra vertical derecha del tablero:
        if coordenada[1] == "9":
            print(" |")
    # Ver la última línea horizontal
    print(trazo_horizontal + "\n\n")


def probar_fin_juego(casillas_jugadas, casillas_ocupadas):
    """Permite probar si el juego ha terminado o no"""
    if len(casillas_ocupadas - casillas_jugadas) == 0:
        print("Bravo. El juego ha terminado !")
        return True

    return False


def crear_barcos():
    barcos = []
    for longitud in LONGITUDES_BARCOS:
        # Un barco se representa por dos coordenadas: letra y numero
        # Estas dos coordenadas son intercambiables:
        #    > una es fija
        #    > otra cambia del inicio al final del barco

        while True:
            # elegir la coordenada fija del barco
            print("Barco len {}, entre {} y {}".format(longitud, list(range(10)), list(range(11-longitud))))
            rang = choice(range(10))
            # Elegir la coordenada del inicio del barco
            primero = choice(range(11-longitud))

            # Determinar ahora cuál será la letra y cuál será el número
            if random() > 0.5:
                # El barco es horizontal
                letra = chr(65 + rang)
                cifras = [str(x) for x in range(primero, primero + longitud)]
                # Crear el barco
                barco = {l + c for l, c in product(repeat(letra, longitud), cifras)}
            else:
                # El barco es vertical
                cifra = str(rang)
                letras = [chr(65 + x) for x in range(primero, primero + longitud)]
                # Crear el barco
                barco = {l + c for l, c in product(letras, repeat(cifra, longitud))}

            for existente in barcos:
                if barco.intersection(existente):
                    # Una casilla del barco se une con un barco existente
                    # El barco no está bien ubicado, se cambia
                    break  # break relativo al "for existente in barcos:"
            else:
                barcos.append(barco)
                break  # break relativo al "while True:"

    return barcos


def jugar_una_partida():
    """Algoritmo de una partida"""
    # Creamos un tablero de juego vacío
    letras = [chr(x) for x in range(65, 75)]
    cifras = [str(x) for x in range(10)]
    casillas = ["".join(x) for x in product(letras, cifras)]

    barcos = crear_barcos()
    print(barcos)
    casillas_ocupadas = reduce(set.union, barcos)

    casillas_jugadas = set()

    while True:
        ver_tabla(letras, cifras, casillas, barcos,
                         casillas_ocupadas, casillas_jugadas)

        casilla = jugar_tirada(casillas_jugadas)
        casillas_jugadas.add(casilla)
        if casilla in casillas_ocupadas:
            for barco in barcos:
                if casilla in barco:
                    # Encontramos el barco tocado
                    if len(barco - casillas_jugadas) == 0:
                        print("Hundido !!")
                    else:
                        print("Tocado !")
                    # Encontramos el barco, no merece la pena mirar el resto
                    break
        else:
            print("Agua !")

        if probar_fin_juego(casillas_jugadas, casillas_ocupadas):
            # Si el juego ha terminado, salimos de la función
            ver_tabla(letras, cifras, casillas, barcos,
                             casillas_ocupadas, casillas_jugadas)
            return


def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? ? [s/n]")


def jugar():
    while True:
        jugar_una_partida()

        if not elegir_jugarOtra():
            return

