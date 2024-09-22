"""
Columba 0.2
https://github.com/jorsaland/columba

This is a back-end Web app capable of scheduling emails.

In version 0.2, the prototype is improved again. Now, a SQL database
stores events which are created, read and updated by the app.
"""


from datetime import timedelta
from uuid import uuid1


from app.constants import valid_time_units, MINUTES, HOURS

from app.entities import Event
from app.repositories.local_sql import EventsRepository, configure_database
from app.utils.convert_time import convert_time


def main():

    """
    Runs the events scheduler.
    """

    configure_database()

    while True:

        print('='*100)

        while True:
            when_str = input('When: ')
            try:
                when = convert_time(when_str)
            except Exception as exception:
                print(exception)
            else:
                break

        message = input('Event message: ')

        while True:
            period_value_str = input('Repeat every (default 0): ')
            if not period_value_str:
                period_value_str = '0'
            try:
                period_value = int(period_value_str)
            except Exception as exception:
                print(exception)
            else:
                break

        if not period_value > 0:
            period_units = MINUTES
        else:
            while True:
                period_units = input('Units (default minutes): ')
                if not period_units:
                    period_units = MINUTES
                if period_units not in valid_time_units:
                    print(f'Valid time units: {", ".join(valid_time_units)}')
                else:
                    break

        if period_units == MINUTES:
            period = timedelta(minutes=period_value)
        elif period_units == HOURS:
            period = timedelta(hours=period_value)
        else:
            period = timedelta(days=period_value)

        event = Event(
            event_id = str(uuid1()),
            first_runtime = when,
            next_runtime = when,
            message = message,
            period = period,
        )
        EventsRepository.create_event(event)


if __name__ == '__main__':
    main()