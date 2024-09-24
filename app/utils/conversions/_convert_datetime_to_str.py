"""
Defines the function that converts input time, which must be in ISO format with minute precision (YYYY-MM-DD hh:mm), to datetime.
"""


from datetime import datetime
import re


from app.utils.exceptions import ValidationError
from app.response_messages import response_message_invalid_runtime_format


def convert_datetime_to_str(value: datetime):

    """
    Converts input time, which must be in ISO format with minute precision (YYYY-MM-DD hh:mm), to datetime.
    """

    second_precision_value = value.isoformat().replace('T', ' ')
    minute_precision_value = second_precision_value[:-3]

    return minute_precision_value