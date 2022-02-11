# -*- coding: utf-8 -*-

import logging
import sys
import tools.settings as settings


def shutdown(properties, properties_path):
    logging.info("Shutting down:")

    if settings.save(properties, properties_path):
        logging.info("Settings saved")
    else:
        logging.error("Settings not saved")

    logging.info("Shutdown complete")
    logging.info("")

    sys.exit()

