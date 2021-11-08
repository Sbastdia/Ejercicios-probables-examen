#!/usr/bin/python3

import argparse

from pyramid.paster import bootstrap

def show_settings(settings):
    print('Here are settings')
    for k, v in settings.items():
        print('%-40s     %-20s' % (k, v))
    print('Done.')


def get_parser():
    # Etapa 1 : definir una función proxy hacia la función principal
    def proxy_show_settings(args):
        """Función proxy hacia show_settings"""
        try:
            env = bootstrap(args.config_uri)
        except:
            print('Configuration file is not valid: %s' % args.config_uri)
            return
        settings, closer = env['registry'].settings, env['closer']
        try:
            show_settings(settings)
        finally:
            closer()

    # Etapa 2 : definir el analizador general
    parser = argparse.ArgumentParser(
        prog = 'show_settings',
        description = """Programa que permite visualizar los argumentos""",
        epilog = """Realizado para el libro Python, los fundamentos del lenguaje"""
    )

    # Añadir las opciones útiles

    parser.add_argument(
        'config_uri',
        help = """archivo de configuration""",
        type = str,
    )


    # Etapa 3 : agregar el enlace entre el analizador y la función proxy para calcul_capital
    parser.set_defaults(func=proxy_show_settings)

    return parser




def main():
    parser = get_parser()
    # Etapa 4 : arrancar el análisis de los argumentos y después del programa.
    args = parser.parse_args()
    args.func(args)


# Fin del programa

