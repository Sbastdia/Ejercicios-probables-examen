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

class Tablero:

    def __init__(self):
        # Creamos un tablero de juego vacío
        self.letras = [chr(x) for x in range(65, 75)]
        self.cifras = [str(x) for x in range(10)]
        self.casillas = ["".join(x) for x in product(self.letras, self.cifras)]
        self._crear_barcos()
        self.casillas_ocupadas = reduce(set.union, self.barcos)
        self.casillas_jugadas = set()

    def _crear_barcos(self):
        self.barcos = []
        for longitud in LONGITUDES_BARCOS:
            # Un barco se representa por dos coordenadas: letra y numero
            # Estas dos coordenadas son intercambiables:
            #    > una es fija
            #    > otra cambia del inicio al final del barco

            while True:
                # elegir la coordenada fija del barco
                rang = choice(range(10))
                # Elegir la coordenada del inicio del barco
                primero = choice(range(11-longitud))

                # Determinar ahora cual será la letra y cual el número
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

                for existente in self.barcos:
                    if barco.intersection(existente):
                        # Una casilla del barco se une con un barco existente
                        # El barco no está bien ubicado, se cambia
                        break  # break relativo al "for existente in barcos:"
                else:
                    self.barcos.append(barco)
                    break  # break relativo al "while True:"

    trazo_horizontal = " --" + "+---" * 10 + "+"

    def ver(self):
        print("   |", " | ".join(self.cifras), "|")

        iter_letras = iter(self.letras)

        for coordenada in self.casillas:
            # Trazo horizontal para cada nueva línea
            if coordenada[1] == "0":
                print(self.trazo_horizontal)
                print(" {}".format(next(iter_letras)), end="")

            # Encontrar la casilla correcta
            if coordenada not in self.casillas_jugadas:
                casilla = CASO_NO_JUGADO
            elif coordenada in self.casillas_ocupadas:
                casilla = CASO_TOCADO
            else:
                casilla = CASO_AGUA

            print(" |", casilla, end="")

            # Ver la barra vertical derecha del tablero:
            if coordenada[1] == "9":
                print(" |")
        # Ver la última línea horizontal
        print(self.trazo_horizontal + "\n\n")


    def probar_fin_juego(self):
        """Permite probar si el juego ha terminado o no"""
        if len(self.casillas_ocupadas - self.casillas_jugadas) == 0:
            print("Bravo. El juego ha terminado !")
            return True

        return False


    def jugar_tirada(self):
        """Permite gestionar el dato introducido de una tirada"""
        while True:
            casilla = solicitar_introducir_casilla(
                "Seleccionar una casilla (letra + cifra)")
            if casilla in self.casillas_jugadas:
                print("Esta casilla ya ha sido jugada, elija otra",
                    file=sys.stderr)
            else:
                self.casillas_jugadas.add(casilla)
                break

        if casilla in self.casillas_ocupadas:
            for barco in self.barcos:
                if casilla in barco:
                    # Encontramos el barco tocado
                    if len(barco - self.casillas_jugadas) == 0:
                        print("Hundido !!")
                    else:
                        print("Tocado !")
                    # Encontramos el barco, no merece la pena mirar el resto
                    break
        else:
            print("Agua !")

def jugar_una_partida():
    """Algoritmo de una partida"""
    # Creamos un tablero de juego vacío

    tablero = Tablero()

    while True:
        tablero.ver()

        tablero.jugar_tirada()

        if tablero.probar_fin_juego():
            # Si el juego ha terminado, salimos de la función
            tablero.ver()
            return


def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? ? [s/n]")


def jugar():
    while True:
        jugar_una_partida()

        if not elegir_jugarOtra():
            return

