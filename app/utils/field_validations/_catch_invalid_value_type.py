"""
Defines the function that catches invalid types in an incoming request field.
"""


from typing import TypeVar


from app.internal_messages import response_message_invalid_field_type
from app.utils.exceptions import ValidationError


Field = TypeVar('Field')


def catch_invalid_value_type(*, field_value, valid_type: type[Field]):

    """
    Catches invalid types in an incoming request field.
    """

    if not isinstance(field_value, valid_type):
        actual_type: type = type(field_value)
        error_message = response_message_invalid_field_type.format(
            valid_type = valid_type.__name__,
            invalid_type = actual_type.__name__,
        )
        raise ValidationError(code=409, message=error_message)
    
    verified_field_value: Field = field_value
    return verified_field_value