"""
Defines the function that builds a filter Event entity from a query parameters dict.
"""


from app.constants import (
    FIELD_EVENT_ID,
    FIELD_STATE,
    FIELD_RUNTIME,
    FIELD_PERIOD,
    FIELD_SENDER_NAME,
    FIELD_SUBJECT,
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
    Builds a filter Event entity from a query parameters dict.
    """

    filter_event = Event()
    error_messages: list[str] = []

    # Event ID

    if (event_id := query_params.get(FIELD_EVENT_ID)) is not None:
        filter_event.event_id = event_id

    # State

    if (state := query_params.get(FIELD_STATE)) is not None:
        try:
            catch_invalid_categorical_value(
                field_value = state,
                categorical_values = valid_states,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_STATE)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            filter_event.state = state

    # Next runtime

    if (input_runtime := query_params.get(FIELD_RUNTIME)) is not None:
        try:
            runtime = convert_str_to_datetime(input_runtime)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            filter_event.runtime = runtime

    # Period

    if (input_period := query_params.get(FIELD_PERIOD)) is not None:
        try:
            period = convert_str_to_timedelta(input_period)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            filter_event.period = period

    # Sender name

    if (sender_name := query_params.get(FIELD_SENDER_NAME)) is not None:
        filter_event.sender_name = sender_name

    # Subject

    if (subject := query_params.get(FIELD_SUBJECT)) is not None:
        filter_event.subject = subject

    # Concatenate error messages

    if switches.REJECT_INVALID_QUERY_PARAMS and error_messages:
        raise ValidationError(code=409, message=' '.join(error_messages))

    # Return filter

    return filter_event