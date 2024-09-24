"""
Columba 0.3
https://github.com/jorsaland/columba

This is where Columba send the messages.

---------------------------------------------------------------------

Please, run both this script and main.py
"""


import schedule


import time
from datetime import datetime


from app.constants import LOGGER_SKETCH_PATH, ACTIVE
from app.entities import Event
from app.repositories.local_sql import EventsRepository, configure_database


def add_log(log: str):

    """
    Adds a log to a file.
    """

    with open(LOGGER_SKETCH_PATH, 'a', newline='\n') as file:
        file.write(f'{log}\n')


def job():

    """
    Logs pending events.
    """

    raw_now = datetime.now()
    now = datetime(
        year = raw_now.year,
        month = raw_now.month,
        day = raw_now.day,
        hour = raw_now.hour,
        minute = raw_now.minute,
    )

    add_log(f'COLUMBA {now}')

    messages: list[str] = []

    query = Event(next_runtime=now, state=ACTIVE)
    for event in EventsRepository.read_events_by_fields(query):

        messages.append(event.message)
        if event.period.total_seconds() > 0:

            next_runtime = event.next_runtime + event.period
            fields_to_update = Event(next_runtime=next_runtime)
            EventsRepository.update_event(event.event_id, fields_to_update)

    for message in messages:
        add_log(f'>>> {message}')


def main():

    """
    Runs the events messenger.
    """

    add_log('===== STARTING COLUMBA =====')
    configure_database()
    for minute in range(60):
        formatted_minute = str(minute).rjust(2, '0')
        schedule.every().hour.at(f':{formatted_minute}').do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()