#!/usr/bin/python3

from gi.repository import Gtk

import argparse

from pyramid.paster import bootstrap
from sqlalchemy import engine_from_config
from contact.models import DBSession, Base, Contact, Subject

import transaction


class GtkContact:
    def __init__(self, controller):
        self.controller = controller

        # Carga de la interface diseñada con Glade
        interface = Gtk.Builder()
        interface.add_from_file('contact/templates/contact.glade')

        # Enlace a los campos útiles        
        self.email = interface.get_object("email_entry")
        self.subject = interface.get_object("subject_id_combobox")
        self.text = interface.get_object("message_textview")

        # Relleno de la lista desplegable
        store = Gtk.ListStore(int, str)
        for subject in controller.get_subjects():
            store.append([subject.id, subject.name])

        self.subject.set_model(store)
        cell = Gtk.CellRendererText()
        self.subject.pack_start(cell, True)
        self.subject.add_attribute(cell, "text", 1)

        # Añadir los eventos a los métodos de la clase
        interface.connect_signals(self)

        # Ver la ventana
        window = interface.get_object("main_window")
        window.show_all()

    def on_main_window_destroy(self, widget):
        Gtk.main_quit()

    def on_apply_button_clicked(self, widget):
        # Recuperación del valor de un campo texte
        email = self.email.get_text()

        # Recuperación del valor de una lista desplegable
        tree_iter = self.subject.get_active_iter()
        if tree_iter is None:
            return
        model = self.subject.get_model()
        row_id, name = model[tree_iter][:2]
        subject_id = row_id

        # Recuperación del valor de un campo de texto multilínea
        message = self.text.get_buffer()
        text = message.get_text(message.get_start_iter(), message.get_end_iter(), False)

        # Creación del contacto
        self.controller.add_contact(email, subject_id, text)


class Controller:
    def __init__(self, DBSession):
        self.DBSession = DBSession
        GtkContact(self)
        Gtk.main()

    def get_subjects(self):
        return DBSession.query(Subject).all()

    def add_contact(self, email, subject_id, text):
        with transaction.manager:
            DBSession.add(Contact(email=email, subject_id=subject_id, text=text))

def get_parser():
    # Etapa 1 : definir una función proxy hacia la función principal
    def proxy_gcontact(args):
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
            Controller(DBSession)
        finally:
            closer()

    # Etapa 2 : definir el analizador general
    parser = argparse.ArgumentParser(
        prog = 'contact',
        description = """Programa que permite agregar un Contacto""",
        epilog = """Realizado para el libro Python, los fundamentos del lenguaje"""
    )

    # Añadir las opciones útiles

    parser.add_argument(
        'config_uri',
        help = """archivo de configuración""",
        type = str,
    )

    # Etapa 3 : agregar el enlace entre el analizador y la función proxy para calcul_capital
    parser.set_defaults(func=proxy_gcontact)

    return parser




def main():
    parser = get_parser()
    # Etapa 4 : arrancar el análisis de los argumentos y después del programa.
    args = parser.parse_args()
    args.func(args)


# Fin del programa

