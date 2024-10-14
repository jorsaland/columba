"""
Defines the function that converts input delta, which must be in format "Ad Bh Cm", where A, B and C are days, hours and minutes respectively.
"""


from datetime import timedelta
import re


from app.constants import MINUTES, HOURS, DAYS
from app.utils.exceptions import ValidationError
from app.internal_messages import response_message_invalid_period_format


def convert_str_to_timedelta(value: str):

    """
    Converts input delta, which must be in format "Ad Bh Cm", where A, B and C are days, hours and minutes respectively.
    """

    pattern = fr'^\d+[{MINUTES}{HOURS}{DAYS}]$'

    delta_map = {
        DAYS: 0,
        HOURS: 0,
        MINUTES: 0
    }

    raw_deltas = value.split(' ')
    for raw_delta in raw_deltas:
        if not raw_delta:
            continue
        if not re.match(pattern, raw_delta):
            raise ValidationError(code=409, message=response_message_invalid_period_format)
        period_units = raw_delta[-1]
        period_value = int(raw_delta[:-1])
        delta_map[period_units] = period_value

    return timedelta(
        days = delta_map[DAYS],
        hours = delta_map[HOURS],
        minutes = delta_map[MINUTES],
    )