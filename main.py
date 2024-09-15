import csv, os


from app.constants import DATABASE_SKETCH_PATH
from app.utils.convert_time import convert_time


def create_event(event_time: str, message: str):

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
    data.append([event_time, message])
    with open(DATABASE_SKETCH_PATH, 'w') as file:
        csv.writer(file, lineterminator='\n').writerows(data)


def main():

    """
    Runs the events scheduler.
    """

    while True:
        print('='*100)
        while True:
            event_time = input('Event time: ')
            try:
                convert_time(event_time)
            except Exception as exception:
                print(exception)
            else:
                break
        message = input('Event message: ')
        create_event(event_time, message)


if __name__ == '__main__':
    main()