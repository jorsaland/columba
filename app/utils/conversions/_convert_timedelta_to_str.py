"""
Defines the function that converts a timedelta to minutes.
"""


from datetime import timedelta


from app.constants import DAYS, HOURS, MINUTES


from ._convert_timedelta_to_int import convert_timedelta_to_int


def convert_timedelta_to_str(value: timedelta):

    """
    Converts a timedelta to minutes.
    """

    total_minutes = convert_timedelta_to_int(value)
    
    total_hours = total_minutes // 60
    minutes = total_minutes % 60

    days = total_hours // 24
    hours = total_hours % 24

    return f'{days}{DAYS} {hours}{HOURS} {minutes}{MINUTES}'