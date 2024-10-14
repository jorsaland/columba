"""
Defines the API control that gets all events or filtered events by query parameters.
"""


from flask import request
from flasgger import swag_from


from app.constants import SWAGGER_FILENAME
from app.request_processing import events_read_from_query_params
from app.internal_messages import response_message_successful
from app.utils.api_response import APIResponse


from .._exception_processing import exception_processing


@exception_processing
@swag_from(SWAGGER_FILENAME)
def control_get_events():

    """
    Gets all events or filtered events by query parameters.
    """

    query_params = request.args.to_dict()
    found_entities = events_read_from_query_params(query_params)

    response = APIResponse(
        code = 200,
        message = response_message_successful.format(method=request.method),
        data = [entity.as_response_dict() for entity in found_entities],
    )
    return response.get_flask_response()