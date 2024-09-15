import schedule


import csv, os, time
from datetime import datetime


from app.constants import DATABASE_SKETCH_PATH, LOGGER_SKETCH_PATH


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

    if os.path.exists(DATABASE_SKETCH_PATH):
        with open(DATABASE_SKETCH_PATH) as file:
            data = list(csv.reader(file))
            for str_event_time, message in data:
                event_time = datetime.fromisoformat(str_event_time)
                if now.isoformat().startswith(event_time.isoformat()):
                    messages.append(message)

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