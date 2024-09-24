"""
Defines the API control that deletes an event by ID.
"""


from flask import request
from flasgger import swag_from


from app.constants import SWAGGER_FILENAME
from app.response_messages import response_message_successful
from app.processing import event_delete_by_id
from app.utils.api_response import APIResponse


from .._exception_processing import exception_processing


@exception_processing
@swag_from(SWAGGER_FILENAME)
def control_delete_event(event_id: str):

    """
    Deletes an event by ID.
    """

    deleted_entity = event_delete_by_id(event_id)

    response = APIResponse(
        code = 200,
        message = response_message_successful.format(method=request.method),
        data = deleted_entity.as_response_dict(),
    )
    return response.get_flask_response()