"""
Defines the function that builds an Event entity to create from a request dict.
"""


from datetime import timedelta
from typing import Any


from app.constants import (
    IO_FIELD_MESSAGE,
    IO_FIELD_PERIOD_UNITS,
    IO_FIELD_PERIOD_VALUE,
    IO_FIELD_RUNTIME,
    IO_FIELD_STATE,
    ACTIVE,
    PAUSED,
    MINUTES,
    HOURS,
    DAYS,
    valid_states,
    valid_period_units,
)

from app.entities import Event

from app.response_messages import base_field_error_message, admin_message_unmanaged_case

from app.utils.conversions import convert_str_to_datetime
from app.utils.exceptions import ValidationError, DevelopmentError
from app.utils.field_validations import catch_invalid_value_type, catch_invalid_categorical_value
from app.utils.generate_id import generate_id

import switches


def build_event_creation_entity(request_dict: dict[str, Any]):

    """
    Builds an Event entity to create from a request dict.
    """

    event_to_create = Event()
    error_messages: list[str] = []

    # Message

    if IO_FIELD_MESSAGE in request_dict.keys():
        try:
            message = catch_invalid_value_type(
                field_value = request_dict[IO_FIELD_MESSAGE],
                valid_type = str,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_MESSAGE)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            event_to_create.message = message

    # First and next runtimes

    if IO_FIELD_RUNTIME in request_dict.keys():
        try:
            input_runtime = catch_invalid_value_type(
                field_value = request_dict[IO_FIELD_RUNTIME],
                valid_type = str,
            )
            runtime = convert_str_to_datetime(input_runtime)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_RUNTIME)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            event_to_create.first_runtime = runtime
            event_to_create.next_runtime = runtime

    # State

    ### Validations
    if IO_FIELD_STATE in request_dict.keys():
        try:
            state = catch_invalid_value_type(
                field_value = request_dict[IO_FIELD_STATE],
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
            event_to_create.state = state
    
    ### Set default state
    else:
        if switches.DEFAULT_ACTIVE:
            event_to_create.state = ACTIVE
        else:
            event_to_create.state = PAUSED

    # Period

    ### Units validations or set default units
    if IO_FIELD_PERIOD_UNITS in request_dict.keys():
        try:
            period_units = catch_invalid_value_type(
                field_value = request_dict[IO_FIELD_PERIOD_UNITS],
                valid_type = str,
            )
            catch_invalid_categorical_value(
                field_value = period_units,
                categorical_values = valid_period_units,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_PERIOD_UNITS)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
            period_units = MINUTES
    else:
        period_units = MINUTES

    ### Units validations or set default units
    if IO_FIELD_PERIOD_VALUE in request_dict.keys():
        try:
            period_value = catch_invalid_value_type(
                field_value = request_dict[IO_FIELD_PERIOD_VALUE],
                valid_type = int,
            )
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=IO_FIELD_PERIOD_VALUE)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
            period_value = 0
    else:
        period_value = 0

    ### Generate timedelta from units and value
    if period_units == MINUTES:
        event_to_create.period = timedelta(minutes=period_value)
    elif period_units == HOURS:
        event_to_create.period = timedelta(hours=period_value)
    elif period_units == DAYS:
        event_to_create.period = timedelta(days=period_value)
    else:
        error_message = admin_message_unmanaged_case.format(case=period_units)
        raise DevelopmentError(error_message)

    # Concatenate error messages

    if error_messages:
        raise ValidationError(code=409, message=' '.join(error_messages))

    # Add event ID and return

    event_to_create.event_id = generate_id()
    return event_to_create