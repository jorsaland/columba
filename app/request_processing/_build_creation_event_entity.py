"""
Defines the function that builds an Event entity to create from a request dict.
"""


from datetime import timedelta
from typing import Any


from app.constants import (
    FIELD_MESSAGE,
    FIELD_PERIOD,
    FIELD_RUNTIME,
    FIELD_TO,
    FIELD_CC,
    FIELD_BCC,
    FIELD_SENDER_NAME,
    FIELD_IS_HTML,
    FIELD_SUBJECT,
    FIELD_STATE,
    ACTIVE,
    PAUSED,
    valid_states,
)

from app.entities import Event

from app.internal_messages import base_field_error_message

from app.utils.conversions import convert_str_to_datetime, convert_str_to_timedelta
from app.utils.exceptions import ValidationError
from app.utils.field_validations import (
    catch_invalid_value_type,
    catch_invalid_elements_type,
    catch_invalid_categorical_value,
    catch_invalid_email_addresses,
)
from app.utils.generate_id import generate_id

import switches


def build_creation_event_entity(request_dict: dict[str, Any]):

    """
    Builds an Event entity to create from a request dict.
    """

    event_to_create = Event()
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
            event_to_create.state = state
    
    else:
        if switches.DEFAULT_ACTIVE:
            event_to_create.state = ACTIVE
        else:
            event_to_create.state = PAUSED

    # Next runtime

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
            event_to_create.runtime = runtime

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
            event_to_create.period = period

    else:
        event_to_create.period = timedelta(0)

    # To

    if (field_value := request_dict.get(FIELD_TO)) is not None:
        try:
            to = catch_invalid_value_type(
                field_value = field_value,
                valid_type = list,
            )
            to = catch_invalid_elements_type(
                elements = to,
                valid_type = str,
            )
            catch_invalid_email_addresses(to)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_TO)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            event_to_create.to = to

    # Carbon copy

    if (field_value := request_dict.get(FIELD_CC)) is not None:
        try:
            cc = catch_invalid_value_type(
                field_value = field_value,
                valid_type = list,
            )
            cc = catch_invalid_elements_type(
                elements = cc,
                valid_type = str,
            )
            catch_invalid_email_addresses(cc)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_CC)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            event_to_create.cc = cc

    # Blind carbon copy

    if (field_value := request_dict.get(FIELD_BCC)) is not None:
        try:
            bcc = catch_invalid_value_type(
                field_value = field_value,
                valid_type = list,
            )
            bcc = catch_invalid_elements_type(
                elements = bcc,
                valid_type = str,
            )
            catch_invalid_email_addresses(bcc)
        except ValidationError as exception:
            error_message_base = base_field_error_message.format(field_name=FIELD_BCC)
            _, error_message_body = exception.args
            error_message = error_message_base + ' ' + error_message_body
            error_messages.append(error_message)
        else:
            event_to_create.bcc = bcc

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
            event_to_create.sender_name = sender_name

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
            event_to_create.subject = subject

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
            event_to_create.is_html = is_html
    
    else:
        event_to_create.is_html = False

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
            event_to_create.message = message

    # Concatenate error messages

    if error_messages:
        raise ValidationError(code=409, message=' '.join(error_messages))

    # Add event ID and counts, and return

    event_to_create.event_id = generate_id()
    event_to_create.counts = 0

    return event_to_create