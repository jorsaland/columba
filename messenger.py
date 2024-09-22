import schedule


import time
from datetime import datetime, timedelta


from app.constants import (
    LOGGER_SKETCH_PATH,
    MINUTES,
    HOURS,
    DAYS,
    valid_time_units
)
from app.entities import Event
from app.repositories.local_sql import EventsRepository


def add_log(log: str):

    """
    Adds a log to log file.
    """

    with open(LOGGER_SKETCH_PATH, 'a', newline='\n') as file:
        file.write(f'{log}\n')


def job():

    """
    Logs pending events.
    """

    now = datetime.now()
    add_log(f'COLUMBA {now}')

    messages: list[str] = []

    for event in EventsRepository.read_all_events():

        time_conditions = [
            now.date() == event.next_runtime.date(),
            now.hour == event.next_runtime.hour,
            now.minute == event.next_runtime.minute,
        ]
        if all(time_conditions):

            messages.append(event.message)
            if event.period.total_seconds() > 0:

                next_runtime = event.next_runtime + event.period
                continuation_event = Event(
                    first_runtime = event.first_runtime,
                    next_runtime = next_runtime,
                    message = event.message,
                    period = event.period,
                )
                EventsRepository.create_event(continuation_event)

    for message in messages:
        add_log(f'>>> {message}')


def main():

    """
    Runs the events messenger.
    """

    add_log('===== INICIANDO COLUMBA =====')
    for minute in range(60):
        formatted_minute = str(minute).rjust(2, '0')
        schedule.every().hour.at(f':{formatted_minute}').do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()