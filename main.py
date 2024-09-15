import csv, os, re
from datetime import datetime


DATABASE_SKETCH_PATH = 'local_database.csv'


def create_event(message: str, event_time: str):

    """
    Adds an event to a local file.
    """

    # Read file
    if os.path.exists(DATABASE_SKETCH_PATH):        
        with open(DATABASE_SKETCH_PATH, 'r') as file:
            data = list(csv.reader(file))
    else:
        data = []

    # Append event and overwrite file
    data.append([message, event_time])
    with open(DATABASE_SKETCH_PATH, 'w') as file:
        csv.writer(file, lineterminator='\n').writerows(data)


def convert_time(event_time: str):

    """
    Converts input time, which must be in ISO format with minute precision (YYYY-MM-DD hh:mm).
    """

    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
    if not re.match(pattern, event_time):
        raise ValueError('time format must be: YYYY-MM-DD hh:mm')
    return datetime.fromisoformat(event_time)


def main():
    while True:
        print('='*100)
        message = input('Event message: ')
        while True:
            event_time = input('Event time: ')
            try:
                convert_time(event_time)
            except Exception as exception:
                print(exception)
            else:
                break
        create_event(message, event_time)


if __name__ == '__main__':
    main()