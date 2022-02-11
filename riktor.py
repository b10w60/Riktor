# -*- coding: utf-8 -*-

# An Autoclicker for Windows, named by an AI

# pyinstaller --noconsole --onefile riktor.py

import os
import sys
import tools.settings as settings
import tools.popups as popups
import logging
import traceback
import ressources.languages.strings

ver = "0.1"

appdatapath = os.getenv('LOCALAPPDATA') + '\\riktor\\'
logfile_path = appdatapath + 'riktor.log'
properties_path = appdatapath + 'riktor_properties.json'

default_properties = {
    "prop_version": "1",
    "sg.theme": "Default 1",
    "language": "en",
}


def startup():
    print("Starting:")
    # appdata anlegen falls noch nicht vorhanden
    print("Checking local files")
    if not os.path.isdir(appdatapath):
        os.mkdir(appdatapath)

    # properties finden und laden
    print("Checking properties")
    props = settings.load(properties_path)
    if not props:
        props = default_properties
        success = settings.reset(props, appdatapath, "riktor_properties.json")
        if not success:
            popups.message("Warning",
                                 "Settings cannot be saved. Using default values.\n"
                                 "These can be changed at runtime\nbut not be saved.")

    # auf änderung prüfen
    if not props["prop_version"] == default_properties["prop_version"]:
        popups.message("Update",
                             "The settings had to be reset!\n"
                             "Please check your settings before continuing!")
        props = default_properties

    # logging konfigurieren und programmstart loggen
    print("Start logging")
    # Erkennung der Python_Version, da das Logging in 3.8 noch keine dekodierung kennt
    if sys.version_info[1] == 9:
        # noinspection PyArgumentList
        logging.basicConfig(filename=logfile_path, encoding='utf-8', level=logging.DEBUG,
                            format='%(asctime)s | %(levelname)s | %(message)s')
    else:
        logging.basicConfig(filename=logfile_path, level=logging.DEBUG,
                            format='%(asctime)s | %(levelname)s | %(message)s')
    logging.info("Starting Riktor " + ver)
    print("Loggin started, echo off")

    # strings importieren
    if props["language"] == "de":
        strings, err_strings = ressources.languages.strings.import_de()
    else:
        strings, err_strings = ressources.languages.strings.import_en()

    return props, strings, err_strings


def main(properties, strings, err_strings):
    print(strings["TEST"])
    pass


# ----------------------------------------------------------------------------------------------------------------------


# start
props, strings, err_strings = startup()

try:
    main(props, strings, err_strings)
except Exception as e:
    logging.critical("*** CRASH ***")
    stack = traceback.format_exc()
    msg = stack.split("\n")
    for i in msg:
        logging.critical(i)
    logging.critical("")
    logging.info("Program terminated, no data saved")
    sys.exit(1)
