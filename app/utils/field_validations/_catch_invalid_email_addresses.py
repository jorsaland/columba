"""
Defines the function that catches an invalid email addresses in a list.
"""


import re


from app.internal_messages import response_message_invalid_email_addresses
from app.utils.exceptions import ValidationError


def catch_invalid_email_addresses(addresses: list[str]):

    """
    Catches invalid email addresses in a list.
    """

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'

    if not all(re.match(pattern, address) for address in addresses):
        raise ValidationError(code=409, message=response_message_invalid_email_addresses)