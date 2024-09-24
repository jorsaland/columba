"""
Defines the class that represents events.
"""


from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any


from app.constants import (
    FIELD_NAME_EVENT_ID,
    FIELD_NAME_NEXT_RUNTIME,
    FIELD_NAME_FIRST_RUNTIME,
    FIELD_NAME_MESSAGE,
    FIELD_NAME_PERIOD,
    FIELD_NAME_STATE,
    IO_FIELD_EVENT_ID,
    IO_FIELD_MESSAGE,
    IO_FIELD_PERIOD,
    IO_FIELD_FIRST_RUNTIME,
    IO_FIELD_NEXT_RUNTIME,
    IO_FIELD_STATE,
    MINUTES,
)

from app.utils.flags import IGNORE_FLAG
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

    event_id: str = IGNORE_FLAG
    state: str = IGNORE_FLAG
    first_runtime: datetime = IGNORE_FLAG
    next_runtime: datetime = IGNORE_FLAG
    message: str = IGNORE_FLAG
    period: timedelta = IGNORE_FLAG


    def as_database_dict(self):

        """
        Converts the event to the format used by the database.
        """

        database_dict: dict[str, Any] = {}

        if self.event_id is not IGNORE_FLAG:
            database_dict[FIELD_NAME_EVENT_ID] = self.event_id
        if self.state is not IGNORE_FLAG:
            database_dict[FIELD_NAME_STATE] = self.state
        if self.first_runtime is not IGNORE_FLAG:
            database_dict[FIELD_NAME_FIRST_RUNTIME] = convert_datetime_to_str(self.first_runtime)
        if self.next_runtime is not IGNORE_FLAG:
            database_dict[FIELD_NAME_NEXT_RUNTIME] = convert_datetime_to_str(self.next_runtime)
        if self.message is not IGNORE_FLAG:
            database_dict[FIELD_NAME_MESSAGE] = self.message
        if self.period is not IGNORE_FLAG:
            database_dict[FIELD_NAME_PERIOD] = convert_timedelta_to_int(self.period)

        return database_dict


    def as_response_dict(self):

        """
        Converts the event to the format used by responses.
        """

        response_dict: dict[str, Any] = {}

        if self.event_id is not IGNORE_FLAG:
            response_dict[IO_FIELD_EVENT_ID] = self.event_id
        if self.state is not IGNORE_FLAG:
            response_dict[IO_FIELD_STATE] = self.state
        if self.first_runtime is not IGNORE_FLAG:
            response_dict[IO_FIELD_FIRST_RUNTIME] = convert_datetime_to_str(self.first_runtime)
        if self.next_runtime is not IGNORE_FLAG:
            response_dict[IO_FIELD_NEXT_RUNTIME] = convert_datetime_to_str(self.next_runtime)
        if self.message is not IGNORE_FLAG:
            response_dict[IO_FIELD_MESSAGE] = self.message
        if self.period is not IGNORE_FLAG:
            response_dict[IO_FIELD_PERIOD] = convert_timedelta_to_str(self.period)

        return response_dict


    @classmethod
    def from_database_dict(cls, database_dict: dict[str, Any]):

        """
        Builds an event from the format used by the database.
        """

        event = Event()

        if (value := database_dict.get(FIELD_NAME_EVENT_ID)) is not None:
            event.event_id = value
        if (value := database_dict.get(FIELD_NAME_STATE)) is not None:
            event.state = value
        if (value := database_dict.get(FIELD_NAME_FIRST_RUNTIME)) is not None:
            event.first_runtime = datetime.fromisoformat(value)
        if (value := database_dict.get(FIELD_NAME_NEXT_RUNTIME)) is not None:
            event.next_runtime = datetime.fromisoformat(value)
        if (value := database_dict.get(FIELD_NAME_MESSAGE)) is not None:
            event.message = value
        if (value := database_dict.get(FIELD_NAME_PERIOD)) is not None:
            event.period = timedelta(minutes=value)

        return event