"""
Defines the function that converts input time, which must be in ISO format with minute precision (YYYY-MM-DD hh:mm), to datetime.
"""


from datetime import datetime
import re


from app.utils.exceptions import ValidationError
from app.internal_messages import response_message_invalid_runtime_format


def convert_str_to_datetime(value: str):

    """
    Converts input time, which must be in ISO format with minute precision (YYYY-MM-DD hh:mm), to datetime.
    """

    pattern_1 = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
    pattern_2 = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$'

    if not (re.match(pattern_1, value) or re.match(pattern_2, value)):
        raise ValidationError(code=409, message=response_message_invalid_runtime_format)

    try:
        return datetime.fromisoformat(value)
    except ValueError:
        raise ValidationError(code=409, message=response_message_invalid_runtime_format)