"""
Defines the function that catches any invalid field names in a request.
"""


from collections.abc import Iterable


from app.response_messages import response_message_invalid_field_names
from app.utils.exceptions import ValidationError


def catch_invalid_fields(*, actual_names: Iterable[str], valid_names: Iterable[str]):

    """
    Catches any invalid field names in a request.
    """

    invalid_names = set(actual_names).difference(set(valid_names))

    if invalid_names:
        error_message = response_message_invalid_field_names.format(
            invalid_names = ', '.join(invalid_names),
            valid_names = ', '.join(valid_names),
        )
        raise ValidationError(code=409, message=error_message)