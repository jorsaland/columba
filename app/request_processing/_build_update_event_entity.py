"""
Defines the function that builds an Event entity to update from a request dict.
"""


from typing import Any


from app.constants import (
    FIELD_MESSAGE,
    FIELD_PERIOD,
    FIELD_RUNTIME,
    FIELD_STATE,
    FIELD_SENDER_NAME,
    FIELD_SUBJECT,
    FIELD_IS_HTML,
    valid_states,
)

from app.entities import Event

from app.internal_messages import base_field_error_message

from app.utils.conversions import convert_str_to_datetime, convert_str_to_timedelta
from app.utils.exceptions import ValidationError
from app.utils.field_validations import catch_invalid_value_type, catch_invalid_categorical_value


def build_update_event_entity(request_dict: dict[str, Any]):

    """
    Builds an Event entity to update from a request dict.
    """

    update_event = Event()
    error_messages: list[str] = []

    # State

    if (field_value := request_dict.get(FIELD_STATE)) is not None:
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
            error_message_base = base_field_error_message.format(field_name=FIELD_STATE)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.state = state

    # Next runtimes

    if (field_value := request_dict.get(FIELD_RUNTIME)) is not None:
        try:
            input_runtime = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
            runtime = convert_str_to_datetime(input_runtime)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.runtime = runtime

    # Period

    if (field_value := request_dict.get(FIELD_PERIOD)) is not None:
        try:
            input_period = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
            period = convert_str_to_timedelta(input_period)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_PERIOD)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.period = period

    # Sender name

    if (field_value := request_dict.get(FIELD_SENDER_NAME)) is not None:
        try:
            sender_name = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_SENDER_NAME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.sender_name = sender_name

    # Subject

    if (field_value := request_dict.get(FIELD_SUBJECT)) is not None:
        try:
            subject = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_SUBJECT)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.subject = subject

    # Is HTML

    if (field_value := request_dict.get(FIELD_IS_HTML)) is not None:
        try:
            is_html = catch_invalid_value_type(
                field_value = field_value,
                valid_type = bool,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_IS_HTML)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.is_html = is_html

    # Message

    if (field_value := request_dict.get(FIELD_MESSAGE)) is not None:
        try:
            message = catch_invalid_value_type(
                field_value = field_value,
                valid_type = str,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_MESSAGE)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            update_event.message = message

    # Concatenate error messages

    if error_messages:
        raise ValidationError(code=409, message=' '.join(error_messages))

    # Add event ID and return

    return update_event