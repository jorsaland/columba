"""
Defines the decorator that runs a controller function and converts exceptions to API responses.
"""


from flask.wrappers import Response


from collections.abc import Callable
from functools import wraps
from traceback import format_exc


from app.response_messages import response_message_soft_unexpected_error, response_message_hard_unexpected_error

from app.utils.exceptions import ValidationError
from app.utils.api_response import APIResponse

import switches


def exception_processing(controller_function: Callable[..., tuple[Response, int]]):

    """
    Runs a controller function and converts exceptions to API responses.
    """

    @wraps(controller_function)
    def wrapper(*args, **kwargs):

        try:

            successful_flask_response = controller_function(*args, **kwargs)
        
        except ValidationError as exception:

            code, error_message = exception.args
            if switches.EXPLICIT_ERROR_RESPONSES:
                code, error_message = exception.args
            else:
                code = 500
                error_message = response_message_soft_unexpected_error

            error_response = APIResponse(
                code = code,
                message = error_message
            )
            return error_response.get_flask_response()
        
        except Exception:

            if switches.EXPLICIT_ERROR_RESPONSES:
                code = 500
                error_message = response_message_hard_unexpected_error.format(full_traceback=format_exc())
            else:
                code = 500
                error_message = response_message_soft_unexpected_error
            
            error_response = APIResponse(
                code = 500,
                message = error_message
            )
            return error_response.get_flask_response()

        else:

            return successful_flask_response

    return wrapper