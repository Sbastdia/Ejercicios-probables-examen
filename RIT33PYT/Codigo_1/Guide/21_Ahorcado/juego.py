"""
Ejercicios : escribir solicitar_introducir_cadena y solicitar_introducir_caracter
Ejercicio : escribir elegir_numero_jugadores, solicitar_numero_jugador
"""


from introducir import (
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
)


def solicitar_numero_jugadores():
    return solicitar_introducir_numero_extremo(
        "Número de jugadores ", 1, 2)


def elegir_palabra():
    return "todo"


def solicitar_introducir_palabra_misterioso():
    return solicitar_introducir_palabra("Indique la palabra a adivinar: ")


def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? [s/n]")


def adivinar_palabra(palabra):
    # Aquí sabemos que la palabra se compone de letras minúsculas,
    # sin acentos, guiones o espacios.

    while True:
        letra = solicitar_introducir_letra("Introduzca una letra: ")
        # También sabemos que la letra es minúscula.

        if letra in palabra:
            print("La letra {} está en la palabra a encontrar".format(letra))
        else:
            print("La letra {} NO está en la palabra a encontrar".format(letra))

        break


def jugar():
    while True:
        if solicitar_numero_jugadores() == 1:
            palabra = elegir_palabra()
        else:
            palabra = solicitar_introducir_palabra_misterioso()

        adivinar_palabra(palabra)
        
        if not elegir_jugarOtra():
            return

