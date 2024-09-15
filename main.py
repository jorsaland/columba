import csv, os


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


def main():
    while True:
        print('='*100)
        message = input('Event message: ')
        event_time = input('Event time: ')
        create_event(message, event_time)


if __name__ == '__main__':
    main()