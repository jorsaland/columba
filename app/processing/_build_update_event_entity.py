"""
Defines the function that builds an Event entity to update from a request dict.
"""


from typing import Any


from app.constants import (
    IO_FIELD_MESSAGE,
    IO_FIELD_PERIOD,
    IO_FIELD_NEXT_RUNTIME,
    IO_FIELD_STATE,
    valid_states,
)

from app.entities import Event

from app.response_messages import base_field_error_message

from app.utils.conversions import convert_str_to_datetime, convert_str_to_timedelta
from app.utils.exceptions import ValidationError
from app.utils.field_validations import catch_invalid_value_type, catch_invalid_categorical_value


def build_update_event_entity(request_dict: dict[str, Any]):

    """
    Builds an Event entity to update from a request dict.
    """

    update_event = Event()
    error_messages: list[str] = []

    # Message

    if (field_value := request_dict.get(IO_FIELD_MESSAGE)) is not None:
        try:
            message = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_MESSAGE)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.message = message

    # Next runtimes

    if (field_value := request_dict.get(IO_FIELD_NEXT_RUNTIME)) is not None:
        try:
            input_runtime = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
            runtime = convert_str_to_datetime(input_runtime)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_NEXT_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.next_runtime = runtime

    # State

    if (field_value := request_dict.get(IO_FIELD_STATE)) is not None:
        try:
            state = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
            catch_invalid_categorical_value(
                field_value = state,
                categorical_values = valid_states,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_STATE)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.state = state

    # Period

    if (field_value := request_dict.get(IO_FIELD_PERIOD)) is not None:
        try:
            input_period = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
            period = convert_str_to_timedelta(input_period)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_PERIOD)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.period = period

    # Concatenate error messages

    if error_messages:
        raise ValidationError(code=409, message=' '.join(error_messages))

    # Add event ID and return

    return update_event