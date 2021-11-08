"""
Exo : Algoritmos adivinar_palabra
"""


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
    return "todo"


def introducir_palabra():
    return solicitar_introducir_palabra("Indique la palabra a adivinar: ")


def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? [s/n]")


def adivinar_palabra(palabra):
    # Aquí sabemos que la palabra se compone de letras minúsculas,
    # sin acentos, guiones o espacios.

    letras_verificadas = ""
    letras_encontradas = ""
    # palabra_oculta = "_" * len(palabra)

    while True:
        # Ver la palabra a adivinar
        print("La palabra a adivinar es '", end="")
        for letra in palabra:
            if letra in letras_verificadas:
                print(letra, end="")
            else:
                print("_", end="")
        print("'.")

        # También sabemos que la letra es minúscula.
        letra = solicitar_introducir_letra("Introduzca una letra: ")

        if letra in letras_verificadas:
            # Ya hemos verificado esta letra
            continue
        # Añadimos la nueva letra a la lista de aquellas que hemos verificado
        letras_verificadas += letra

        # Verificar la presencia de la letra
        if letra in palabra:
            letras_encontradas += letra
            num_ocurrencias = palabra.count(letra)
            print("La letra {} está {} en la palabra a encontrar".format(
                letra, num_ocurrencias))
        else:
            num_ocurrencias = 0
            print("La letra {} NO está en la palabra a encontrar".format(letra))

        # Cálculo de la posición de las letras y visualización en la palabra oculta
        posicion = -1
        for _ in range(num_ocurrencias):
            posicion = palabra.find(letra, posicion + 1)
            print("La letra es trouvée a la posicion {}".format(posicion))

        #if num_ocurrencias > 0:
        #    nueva_palabra_oculta = ""
        #    for palabra_oculta_indice, palabra_oculta_letra in enumerate(palabra_oculta):
        #        if palabra_oculta_indice in posiciones:
        #            nueva_palabra_oculta += letra
        #        else:
        #            nueva_palabra_oculta += palabra_oculta_letra
        #    palabra_oculta = nueva_palabra_oculta
        #print("La palabra a adivinar es {}".format(palabra_oculta))

        # ¿He ganado?
        #if "_" in lista_letras_oculta:
        #    print("Letras jugadas: {}", ", ".join(letras_verificadas))
        #else:
        #    print("Victoria")
        #    return

        # ¿He ganado?
        for letra in palabra:
            if letra not in palabra:
                print("Letras jugadas: '{}'.".format(letras_verificadas))
                break
        else:
            print("Victoria, la palabra era '{}'".format(palabra))
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


