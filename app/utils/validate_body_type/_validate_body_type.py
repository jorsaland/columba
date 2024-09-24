"""
Defines the function that validates expected request body type.
"""


from werkzeug import Request
from werkzeug.exceptions import UnsupportedMediaType


from typing import TypeVar


from app.constants import json_valid_types
from app.response_messages import (
    admin_message_not_pythonifyable_request,
    response_message_bad_request_body,
    response_message_no_request_body,
)
from app.utils.exceptions import ValidationError, DevelopmentError


RequestBody = TypeVar('RequestBody')


def validate_body_type(*, request: Request, valid_type: type[RequestBody]):

    """
    Validates expected request body type.
    """

    if valid_type not in json_valid_types:
        raise DevelopmentError(admin_message_not_pythonifyable_request.format(type=valid_type))

    try:
        request_body = request.json
    except UnsupportedMediaType:
        raise ValidationError(code=400, message=response_message_no_request_body)

    if not isinstance(request_body, valid_type):
        raise ValidationError(code=400, message=response_message_bad_request_body)
    
    verified_body: RequestBody = request_body
    return verified_body