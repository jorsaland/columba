"""
Columba 0.6
https://github.com/jorsaland/columba

This is where Columba send the messages.

---------------------------------------------------------------------

Please, run both this script and main.py
"""


import schedule


import time
import logging


from app.deliver_mails import deliver_mails

from app.repositories.local_sql import configure_database

from app.internal_messages import logger_message_starting_messenger
from app.utils.env_variables import check_env_vars
from app.utils.logger import get_logger

import switches


logger = get_logger()


def main():

    """
    Runs the events messenger.
    """

    if switches.CHECK_ENV_VARS:
        check_env_vars()

    logging.getLogger('schedule').propagate = False
    logger.info(logger_message_starting_messenger)
    configure_database()

    schedule.every().minute.at(':00').do(deliver_mails)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()