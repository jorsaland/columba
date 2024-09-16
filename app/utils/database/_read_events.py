"""
Defines the function that reads all the events in the database.
"""


import csv, os
from datetime import datetime


from app.constants import DATABASE_SKETCH_PATH


def read_events():

    """
    Reads all the events in the database.
    """

    if not os.path.exists(DATABASE_SKETCH_PATH):
        data = []
        return data

    with open(DATABASE_SKETCH_PATH) as file:

        str_data = list(csv.reader(file))
        data: list[tuple[datetime, str, int, str]] = []

        for when_str, message, period_value_str, period_units in str_data:
            when = datetime.fromisoformat(when_str)
            period_value = int(period_value_str)
            data.append((when, message, period_value, period_units))

    return data