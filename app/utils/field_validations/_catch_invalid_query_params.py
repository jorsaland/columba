"""
Define la función que valida que no haya parámetros de consulta inválidos.
"""


from collections.abc import Iterable


from app.response_messages import response_message_invalid_query_params
from app.utils.exceptions import ValidationError


def catch_invalid_query_params(*, actual_names: Iterable[str], valid_names: Iterable[str]):

    """
    Valida que no haya parámetros de consulta inválidos.
    """

    invalid_names: list[str] = []

    for query_field in actual_names:
        if query_field not in valid_names:
            invalid_names.append(query_field)
    
    if invalid_names:
        error_message = response_message_invalid_query_params.format(
            invalid_names = ', '.join(invalid_names),
            valid_names = ', '.join(valid_names),
        )
        raise ValidationError(code=409, message=error_message)