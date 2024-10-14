"""
Defines the function that catches invalid types for all the elements in an incoming request field.
"""


from typing import TypeVar


from app.internal_messages import response_message_invalid_elements_type
from app.utils.exceptions import ValidationError


Field = TypeVar('Field')


def catch_invalid_elements_type(*, elements: list, valid_type: type[Field]):

    """
    Catches invalid types for all the elements in an incoming request field.
    """

    if not all(isinstance(element, valid_type) for element in elements):
        error_message = response_message_invalid_elements_type.format(valid_type=valid_type.__name__)
        raise ValidationError(code=409, message=error_message)
    
    verified_elements: list[Field] = elements
    return verified_elements