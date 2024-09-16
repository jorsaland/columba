"""
Defines the function that adds an event to a local file.
"""


import csv, os
from datetime import datetime


from app.constants import DATABASE_SKETCH_PATH


def create_event(*, when: datetime, message: str, period_value: int, period_units: str):

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
    data.append([when.isoformat(), message, str(period_value), period_units])
    with open(DATABASE_SKETCH_PATH, 'w') as file:
        csv.writer(file, lineterminator='\n').writerows(data)