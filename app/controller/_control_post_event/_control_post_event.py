"""
Defines the API control that creates an event from a request body.
"""


from flask import request
from flasgger import swag_from


from app.constants import SWAGGER_FILENAME

from app.internal_messages import response_message_successful

from app.request_processing import event_create_from_request_dict

from app.utils.validate_body_type import validate_body_type
from app.utils.api_response import APIResponse


from .._exception_processing import exception_processing


@exception_processing
@swag_from(SWAGGER_FILENAME)
def control_post_event():

    """
    Creates an event from a request body.
    """

    request_body = validate_body_type(request=request, valid_type=dict)
    created_entity = event_create_from_request_dict(request_body)

    response = APIResponse(
        code = 200,
        message = response_message_successful.format(method=request.method),
        data = created_entity.as_response_dict()
    )
    return response.get_flask_response()