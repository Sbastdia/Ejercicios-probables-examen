from random import choice

from introducir import (
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
)


def elegir_numero_jugadores():
    return solicitar_introducir_numero_extremo(
        "Número de jugadores ", 1, 2)


def elegir_palabra():
    with open("data/test.txt") as f:
        datas = f.readlines()
    return choice(datas)[:-1]


def introducir_palabra():
    return solicitar_introducir_palabra("Indique la palabra a adivinar: ")


def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? [s/n]")


def adivinar_palabra(palabra):
    # Aquí sabemos que la palabra se compone de letras minúsculas,
    # sin acentos, guiones o espacios.

    letras_verificadas = []
    letras_encontradas = []
    lista_letras = list(palabra)
    lista_letras_oculta = ["_"] * len(palabra)

    while True:
        print("La palabra a adivinar es {}".format("".join(lista_letras_oculta)))

        # También sabemos que la letra es minúscula.
        letra = solicitar_introducir_letra("Introduzca una letra: ")

        if letra in letras_verificadas:
            # Ya hemos verificado esta letra
            continue
        # Añadimos la nueva letra a la lista de aquellas que hemos verificado
        letras_verificadas.append(letra)

        # Verificar la presencia de la letra
        if letra in lista_letras:
            letras_encontradas.append(letra)
            num_ocurrencias = lista_letras.count(letra)
            print("La letra {} está {} en la palabra a encontrar".format(
                letra, num_ocurrencias))
        else:
            num_ocurrencias = 0
            print("La letra {} NO está en la palabra a encontrar".format(letra))

        # Cálculo de la posición de las letras y visualización en la palabra oculta
        posicion = -1
        for _ in range(num_ocurrencias):
            posicion = lista_letras.index(letra, posicion + 1)
            lista_letras_oculta[posicion] = letra

        # ¿He ganado?
        if "_" in lista_letras_oculta:
            print("Letras jugadas: {}", ", ".join(letras_verificadas))
        else:
            print("Victoria, la palabra a adivinar era {}".format("".join(lista_letras_oculta)))
            return


def jugar():
    while True:
        if elegir_numero_jugadores() == 1:
            palabra = elegir_palabra()
        else:
            palabra = introducir_palabra()

        adivinar_palabra(palabra)
        
        if not elegir_jugarOtra():
            return


