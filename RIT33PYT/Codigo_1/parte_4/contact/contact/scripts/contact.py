#!/usr/bin/python3

import argparse

from pyramid.paster import bootstrap
from sqlalchemy import engine_from_config
from contact.models import DBSession, Base, Contact, Subject

import transaction

def contact(DBSession, email, subject, text):
    """Add a contacto"""
    obj = DBSession.query(Subject).filter_by(name=subject).first()
    if not obj:
        print('Pick a subject in this list:')
        for obj in DBSession.query(Subject).all():
            print('> %s' % obj.name)
        print('Try again.')
        return
    with transaction.manager:
        DBSession.add(Contact(email=email, subject_id=obj.id, text=text))

def get_parser():
    # Etapa 1 : definir una función proxy hacia la función principal
    def proxy_contact(args):
        """Función proxy hacia contacto"""
        try:
            env = bootstrap(args.config_uri)
        except:
            print('Configuration file is not valid: %s' % args.config_uri)
            return
        settings, closer = env['registry'].settings, env['closer']
        try:
            engine = engine_from_config(settings, 'sqlalchemy.')
            DBSession.configure(bind=engine)
            Base.metadata.bind = engine
            contact(DBSession, args.email, args.subject, args.text)
        finally:
            closer()

    # Etapa 2 : definir el analizador general
    parser = argparse.ArgumentParser(
        prog = 'contact',
        description = """Programa que permiten agregar un Contacto""",
        epilog = """Realizado para el libro Python, los fundamentos del lenguaje"""
    )

    # Añadir las opciones útiles

    parser.add_argument(
        'config_uri',
        help = """archivo de configuration""",
        type = str,
    )

    parser.add_argument(
        'email',
        help = """Dirección electrónica""",
        type = str,
    )
    parser.add_argument(
        'subject',
        help = """Asunto""",
        type = str,
    )
    parser.add_argument(
        'text',
        help = """Mensaje""",
        type = str,
    )


    # Etapa 3 : agregar el enlace entre el analizador y la función proxy para calcul_capital
    parser.set_defaults(func=proxy_contact)

    return parser




def main():
    parser = get_parser()
    # Etapa 4 : arrancar el análisis de los argumentos y después del programa.
    args = parser.parse_args()
    args.func(args)


# Fin del programa

