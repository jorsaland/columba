"""
Defines the function that builds an Event entity to create from a request dict.
"""


from app.constants import (
    IO_FIELD_EVENT_ID,
    IO_FIELD_STATE,
    IO_FIELD_FIRST_RUNTIME,
    IO_FIELD_NEXT_RUNTIME,
    IO_FIELD_PERIOD,
    valid_states,
)

from app.entities import Event

from app.response_messages import base_field_error_message

from app.utils.conversions import convert_str_to_datetime, convert_str_to_timedelta
from app.utils.exceptions import ValidationError
from app.utils.field_validations import catch_invalid_categorical_value

import switches


def build_filter_event_entity(query_params: dict[str, str]):

    """
    Builds a filter Event entity from a request dict.
    """

    filter_event = Event()
    error_messages: list[str] = []

    # Event ID

    if IO_FIELD_EVENT_ID in query_params.keys():
        filter_event.event_id = query_params[IO_FIELD_EVENT_ID]

    # State

    if (state := query_params.get(IO_FIELD_STATE)) is not None:
        try:
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
            filter_event.event_id = state

    # First runtime

    if (input_first_runtime := query_params.get(IO_FIELD_FIRST_RUNTIME)) is not None:
        try:
            first_runtime = convert_str_to_datetime(input_first_runtime)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_FIRST_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            filter_event.first_runtime = first_runtime

    # Next runtime

    if (input_next_runtime := query_params.get(IO_FIELD_NEXT_RUNTIME)) is not None:
        try:
            next_runtime = convert_str_to_datetime(input_next_runtime)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_NEXT_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            filter_event.next_runtime = next_runtime

    # Period

    if (input_period := query_params.get(IO_FIELD_PERIOD)) is not None:
        try:
            period = convert_str_to_timedelta(input_period)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_NEXT_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            filter_event.period = period

    # Concatenate error messages

    if switches.REJECT_INVALID_QUERY_PARAMS and error_messages:
        raise ValidationError(code=409, message=' '.join(error_messages))

    # Return filter

    return filter_event