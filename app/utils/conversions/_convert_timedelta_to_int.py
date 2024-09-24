"""
Defines the function that converts a timedelta to minutes.
"""


from datetime import timedelta


def convert_timedelta_to_int(value: timedelta):

    """
    Converts a timedelta to minutes.
    """

    seconds = int(value.total_seconds())
    minutes = seconds // 60

    return minutes