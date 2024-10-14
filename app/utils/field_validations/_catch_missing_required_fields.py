"""
Defines the function that catches any missing field names in a request.
"""


from collections.abc import Iterable
from typing import Any


from app.internal_messages import response_message_missing_required_fields
from app.utils.exceptions import ValidationError


def catch_missing_required_fields(*, request_dict: dict[str, Any], required_names: Iterable[str]):

    """
    Catches any missing field names in a request.
    """
    
    missing_required_fields: list[str] = []

    for required_name in required_names:
        if required_name not in request_dict.keys() or request_dict[required_name] is None:
            missing_required_fields.append(required_name)

    if missing_required_fields:
        error_message = response_message_missing_required_fields.format(missing_required_fields=', '.join(missing_required_fields))
        raise ValidationError(code=409, message=error_message)