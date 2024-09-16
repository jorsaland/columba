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
from app.utils.database import create_event, read_events


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

    for when, message, period_value, period_units in read_events():

        time_conditions = [
            now.date() == when.date(),
            now.hour == when.hour,
            now.minute == when.minute,
        ]
        if all(time_conditions):

            messages.append(message)
            if period_value > 0:

                if period_units == MINUTES:
                    continuation_when = when + timedelta(minutes=period_value)
                elif period_units == HOURS:
                    continuation_when = when + timedelta(hours=period_value)
                elif period_units == DAYS:
                    continuation_when = when + timedelta(days=period_value)
                else:
                    add_log(f'!!! CORRUPTED EVENT: period units must be {", ".join(valid_time_units)}, not {period_units}')
                    continue

                create_event(
                    when = continuation_when,
                    message = message,
                    period_value = period_value,
                    period_units = period_units,
                )

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