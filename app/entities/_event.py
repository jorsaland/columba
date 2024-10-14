"""
Defines the class that represents events.
"""


from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any


from app.constants import (
    FIELD_EVENT_ID,
    FIELD_STATE,
    FIELD_COUNTS,
    FIELD_RUNTIME,
    FIELD_PERIOD,
    FIELD_TO,
    FIELD_CC,
    FIELD_BCC,
    FIELD_SENDER_NAME,
    FIELD_SUBJECT,
    FIELD_IS_HTML,
    FIELD_MESSAGE,
)

from app.utils.conversions import (
    convert_timedelta_to_int,
    convert_timedelta_to_str,
    convert_datetime_to_str,
)


@dataclass
class Event:


    """
    Represents events.
    """

    event_id: (str|None) = None
    state: (str|None) = None
    counts: (int|None) = None

    runtime: (datetime|None) = None
    period: (timedelta|None) = None

    to: (list[str]|None) = None
    cc: (list[str]|None) = None
    bcc: (list[str]|None) = None

    sender_name: (str|None) = None
    subject: (str|None) = None
    is_html: (bool|None) = None
    message: (str|None) = None


    def as_database_dict(self):

        """
        Converts the event to the format used by the database.
        """

        database_dict: dict[str, Any] = {}

        if self.event_id is not None:
            database_dict[FIELD_EVENT_ID] = self.event_id
        if self.state is not None:
            database_dict[FIELD_STATE] = self.state
        if self.counts is not None:
            database_dict[FIELD_COUNTS] = self.counts
        if self.runtime is not None:
            database_dict[FIELD_RUNTIME] = convert_datetime_to_str(self.runtime)
        if self.period is not None:
            database_dict[FIELD_PERIOD] = convert_timedelta_to_int(self.period)
        if self.to is not None:
            database_dict[FIELD_TO] = ','.join(self.to)
        if self.cc is not None:
            database_dict[FIELD_CC] = ','.join(self.cc)
        if self.bcc is not None:
            database_dict[FIELD_BCC] = ','.join(self.bcc)
        if self.sender_name is not None:
            database_dict[FIELD_SENDER_NAME] = self.sender_name
        if self.subject is not None:
            database_dict[FIELD_SUBJECT] = self.subject
        if self.is_html is not None:
            database_dict[FIELD_IS_HTML] = self.is_html
        if self.message is not None:
            database_dict[FIELD_MESSAGE] = self.message

        return database_dict


    def as_response_dict(self):

        """
        Converts the event to the format used by responses.
        """

        response_dict: dict[str, Any] = {}

        if self.event_id is not None:
            response_dict[FIELD_EVENT_ID] = self.event_id
        if self.state is not None:
            response_dict[FIELD_STATE] = self.state
        if self.counts is not None:
            response_dict[FIELD_COUNTS] = self.counts
        if self.runtime is not None:
            response_dict[FIELD_RUNTIME] = convert_datetime_to_str(self.runtime)
        if self.period is not None:
            response_dict[FIELD_PERIOD] = convert_timedelta_to_str(self.period)
        if self.to is not None:
            response_dict[FIELD_TO] = self.to
        if self.cc is not None:
            response_dict[FIELD_CC] = self.cc
        if self.bcc is not None:
            response_dict[FIELD_BCC] = self.bcc
        if self.sender_name is not None:
            response_dict[FIELD_SENDER_NAME] = self.sender_name
        if self.subject is not None:
            response_dict[FIELD_SUBJECT] = self.subject
        if self.is_html is not None:
            response_dict[FIELD_IS_HTML] = self.is_html
        if self.message is not None:
            response_dict[FIELD_MESSAGE] = self.message

        return response_dict


    @classmethod
    def from_database_dict(cls, database_dict: dict[str, Any]):

        """
        Builds an event from the format used by the database.
        """

        event = Event()

        if (value := database_dict.get(FIELD_EVENT_ID)) is not None:
            event.event_id = value
        if (value := database_dict.get(FIELD_STATE)) is not None:
            event.state = value
        if (value := database_dict.get(FIELD_COUNTS)) is not None:
            event.counts = value
        if (value := database_dict.get(FIELD_RUNTIME)) is not None:
            event.runtime = datetime.fromisoformat(value)
        if (value := database_dict.get(FIELD_PERIOD)) is not None:
            event.period = timedelta(minutes=value)
        if (value := database_dict.get(FIELD_TO)) is not None:
            event.to = value.split(',')
        if (value := database_dict.get(FIELD_CC)) is not None:
            event.cc = value.split(',')
        if (value := database_dict.get(FIELD_BCC)) is not None:
            event.bcc = value.split(',')
        if (value := database_dict.get(FIELD_SENDER_NAME)) is not None:
            event.sender_name = value
        if (value := database_dict.get(FIELD_SUBJECT)) is not None:
            event.subject = value
        if (value := database_dict.get(FIELD_IS_HTML)) is not None:
            event.is_html = value
        if (value := database_dict.get(FIELD_MESSAGE)) is not None:
            event.message = value

        return event