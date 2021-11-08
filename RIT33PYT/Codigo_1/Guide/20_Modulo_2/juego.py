"""
Módulo que agrupa las funciones que describen la lógica del juego
"""

from introducir import (
    solicitar_introducir_numero,
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
)


def jugar_tirada(numero, minimum, maximum):
    intento = solicitar_introducir_numero_extremo("Adivine el número", minimum, maximum)

    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimum = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximum = intento - 1
        victoria = False
    else:
        print("Victoria!")
        victoria = True
        minimum = maximum = intento
    return victoria, minimum, maximum


def solicitar_introducir_el_numero_misterioso(minimum, maximum):
    return solicitar_introducir_numero_extremo("Introduzca el número a adivinar",
                                        minimum, maximum)


def jugar_una_partida(numero, minimum, maximum):
    while True:
        # Entramos en un bucle infinito
        # que permite jugar varios turnos

        victoria, minimum, maximum = jugar_tirada(numero, minimum, maximum)

        if (victoria):
            return


def decidir_extremos():
    while True:
        minimum = solicitar_introducir_numero("¿Cuál es el extremo mínimo ?")
        maximum = solicitar_introducir_numero("¿Cuál es el extremo máximo ?")
        if maximum > minimum:
            return minimum, maximum


def jugar():
    minimum, maximum = decidir_extremos()
    while True:
        numero = solicitar_introducir_el_numero_misterioso(minimum, maximum)
        jugar_una_partida(numero, minimum, maximum)
        if not solicitar_introducir_si_o_no("¿Desea volver a jugar?"):
            print("Hasta pronto !")
            return

