"""
Defines the function that retrieves the app logger.
"""


import logging


from app.constants import (
    LOGGER_NAME,
    LOGGER_FORMAT,
    LOGGER_LEVEL,
    LOG_FILE_NAME,
)
import switches


level_by_name = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}


def get_logger():

    """
    Retrieves the app logger.
    """

    logger = logging.getLogger(LOGGER_NAME)

    level = level_by_name[LOGGER_LEVEL]
    if switches.LOG_TO_FILE:
        filename = LOG_FILE_NAME
    else:
        filename = None

    logging.basicConfig(style='{', format=LOGGER_FORMAT, level=level, filename=filename)

    return logger