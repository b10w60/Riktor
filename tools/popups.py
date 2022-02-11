# -*- coding: utf-8 -*-

"""
Verschiedene Popups zur Nutzerinteraktion oder -Information
"""

import PySimpleGUIQtCustom as sg

popup_ok_btn_size = (80, 30)
gui_font = "Segoe"
h1 = (gui_font, 14)
console_font = ("Consolas", 10)


def message(title: str, text):
    """
    Zeigt ein Popup-Fenster mit einer Nachricht zur Kenntnisnahme und einem OK-Button

    :param title: Fenstertitel
    :param text: Die Nachricht zur Kenntnisnahme
    :return: nichts
    """

    layout = [
        [sg.Text("")],
        [sg.Text(text)],
        [sg.Text("")],
        [sg.Button("OK", size_px=popup_ok_btn_size)],
    ]

    popup = sg.Window(str(title), layout)
    while True:
        e, v = popup.read()
        if e == "OK" or e == sg.WINDOW_CLOSED:
            break

    popup.close()
    return


def yes_no(title: str, text, option_a="Ja", option_b="Nein"):
    """
    Zeigt ein Popup-Fenster mit einer Nachricht und zwei Buttons als Antwortoptionen.
    Wenn für die options kein String übermittelt wird, werden Standartwerte genommen.

    :param title: Fenstertitel
    :param text: Dialogtext
    :param option_a: Gibt True zurück wenn angeklickt
    :param option_b: Gibt False zurück wenn angeklickt
    :return: True oder False
    """
    layout = [
        [sg.Text("")],
        [sg.Text(text)],
        [sg.Text("")],
        [sg.Button(option_a, size_px=popup_ok_btn_size), sg.Button(option_b, size_px=popup_ok_btn_size)],
    ]

    popup = sg.Window(title, layout)
    while True:
        e, v = popup.read()
        if e == "Nein" or e == sg.WINDOW_CLOSED:
            popup.close()
            return False
        if e == "Ja":
            popup.close()
            return True


def debug_dict(dict_name, mydict, title="DEBUG DICT"):
    """
    Nimmt ein dict entgegen und listet den Inhalt mit fester Laufweite und so dass man ihn kopieren kann
    :param dict_name: Name des dicts
    :param mydict: das eigentliche dict
    :param title: (optional) Fenstertitel
    :return: nichts
    """
    output_content = ""
    for i in mydict:
        output_content = output_content + str(i) + ": " + str(mydict[i]) + "\n"

    layout = [
        [sg.Text('Inhalt vom Dictionary "' + dict_name + '"')],
        [sg.Text("")],
        [sg.MultilineOutput(output_content, font=console_font, size_px=(800, 800))],
        [sg.Text("")],
        [sg.Button("OK", size_px=popup_ok_btn_size)],
    ]

    popup = sg.Window(str(title), layout)
    while True:
        e, v = popup.read()
        if e == "OK" or e == sg.WINDOW_CLOSED:
            break

    popup.close()
    return


def debug_table(table_name, mytable, title="DEBUG TABLE"):
    output_content = ""
    for i in mytable:
        output_content = output_content + str(i) + "\n"

    layout = [
        [sg.Text('Inhalt vom Table "' + table_name + '"')],
        [sg.Text("")],
        [sg.MultilineOutput(output_content, font=console_font, size_px=(800, 800))],
        [sg.Text("")],
        [sg.Button("OK", size_px=popup_ok_btn_size)],
    ]

    popup = sg.Window(str(title), layout)
    while True:
        e, v = popup.read()
        if e == "OK" or e == sg.WINDOW_CLOSED:
            break

    popup.close()
    return


def crash(title, err, trace, addendum=""):
    layout = [
        [sg.Text("Ein nicht behebbarer Fehler ist aufgetreten:")],
        [sg.Text(str(err), font=h1)],
        [sg.Text("")],
        [sg.Text("Stack-Trace zur oben genannten Fehlermeldung:")],
        [sg.MultilineOutput(str(trace), font=console_font)],
        [sg.Text("")],
        [sg.Text(addendum)],
        [sg.Text("")],
        [sg.Button("OK", size_px=popup_ok_btn_size)]
    ]

    popup = sg.Window(str(title), layout)
    while True:
        e, v = popup.read()
        if e == "OK" or e == sg.WINDOW_CLOSED:
            break

    popup.close()
    return


if __name__ == "__main__":
    print("Direkter aufruf von popups.py")
    message("Test", "Direkter aufruf von popups.py")
