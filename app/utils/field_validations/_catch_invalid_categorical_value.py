"""
Define la función que valida que un campo categórico tenga un valor correcto.
"""


from collections.abc import Iterable


from app.internal_messages import response_message_invalid_categorical_value
from app.utils.exceptions import ValidationError


def catch_invalid_categorical_value(*, field_value: str, categorical_values: Iterable[str]):

    """
    Valida que un campo categórico tenga un valor correcto.
    """

    if field_value not in categorical_values:

        error_message = response_message_invalid_categorical_value.format(
            invalid_value = field_value,
            categorical_values = ', '.join(categorical_values),
        )        
        raise ValidationError(code=409, message=error_message)