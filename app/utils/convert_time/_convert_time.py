"""
Converts input time, which must be in ISO format with minute precision (YYYY-MM-DD hh:mm).
"""


from datetime import datetime
import re


def convert_time(event_time: str):

    """
    Converts input time, which must be in ISO format with minute precision (YYYY-MM-DD hh:mm).
    """

    pattern_1 = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
    pattern_2 = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$'
    if not (re.match(pattern_1, event_time) or re.match(pattern_2, event_time)):
        raise ValueError('time format must be: YYYY-MM-DD hh:mm')
    return datetime.fromisoformat(event_time)