# -*- coding: utf-8 -*-

"""
Settings verwalten

Gibt bei load() ein dict zurück
Nimmt bei save() ein dict und einen path entgegen und macht daraus ein json
Erstellt bei reset() eine neues verzeichnis und geht dann ein mal durch save()
"""

import json
import os


def load(file_path):
    """
    Lädt eine json-Datei von der Festplatte, macht daraus ein dict und gibt es zurück
    :param file_path: Pfad zur Datei
    :return: dict
    """
    try:
        f = open(file_path, "r", encoding="utf-8")
    except Exception:
        return False
    content = f.read()
    f.close()
    try:
        return json.loads(content)
    except:
        return False


def save(properties, file_path):
    """
    Nimmt ein Dictionary engtegen und wandelt es in ein json um, speichert es dann.
    :param properties: das Dictionary
    :param file_path: der Pfad unter dem das JSON gespeichert werden soll
    :return: True wenn erfolgreich gespeichert, sonst False
    """
    try:
        f = open(file_path, "w", encoding="utf-8")
    except Exception:
        return False
    content = json.dumps(properties, indent=4)
    f.write(content)
    f.close()
    return True


def reset(properties, file_path, filename):
    """
    Legt Verzeichnis für neue Properties-Datei an.
    :param properties: Das Properties-Dictionary
    :param file_path: Dateipfad
    :param filename: Dateiname
    :return: True wenn erfolgreich, anstonsten False
    """
    try:
        os.mkdir(file_path)
    except FileExistsError:
        pass
    except Exception as e:
        print("Propertydatei konnte nicht erstellt werden.")
        print(e)
        return False
    return save(properties, file_path + filename)


if __name__ == "__main__":
    pass
