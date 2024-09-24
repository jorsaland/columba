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
    IO_FIELD_PERIOD_UNITS,
    IO_FIELD_PERIOD_VALUE,
    IO_FIELD_FIRST_RUNTIME,
    IO_FIELD_NEXT_RUNTIME,
    IO_FIELD_STATE,
    MINUTES,
)
from app.utils.conversions import convert_timedelta_to_int


@dataclass
class Event:


    """
    Represents events.
    """

    event_id: str = None
    state: str = None
    first_runtime: datetime = None
    next_runtime: datetime = None
    message: str = None
    period: timedelta = None


    def as_database_dict(self):

        """
        Converts the event to the format used by the database.
        """

        database_dict: dict[str, Any] = {}

        if self.event_id is not None:
            database_dict[FIELD_NAME_EVENT_ID] = self.event_id
        if self.state is not None:
            database_dict[FIELD_NAME_STATE] = self.state
        if self.first_runtime is not None:
            database_dict[FIELD_NAME_FIRST_RUNTIME] = self.first_runtime.isoformat()
        if self.next_runtime is not None:
            database_dict[FIELD_NAME_NEXT_RUNTIME] = self.next_runtime.isoformat()
        if self.message is not None:
            database_dict[FIELD_NAME_MESSAGE] = self.message
        if self.period is not None:
            database_dict[FIELD_NAME_PERIOD] = convert_timedelta_to_int(self.period)

        return database_dict


    def as_response_dict(self):

        """
        Converts the event to the format used by responses.
        """

        response_dict: dict[str, Any] = {}

        if self.event_id is not None:
            response_dict[IO_FIELD_EVENT_ID] = self.event_id
        if self.state is not None:
            response_dict[IO_FIELD_STATE] = self.state
        if self.first_runtime is not None:
            response_dict[IO_FIELD_FIRST_RUNTIME] = self.first_runtime.isoformat()
        if self.next_runtime is not None:
            response_dict[IO_FIELD_NEXT_RUNTIME] = self.next_runtime.isoformat()
        if self.message is not None:
            response_dict[IO_FIELD_MESSAGE] = self.message
        if self.period is not None:
            response_dict[IO_FIELD_PERIOD_VALUE] = convert_timedelta_to_int(self.period)
        if self.period is not None:
            response_dict[IO_FIELD_PERIOD_UNITS] = MINUTES

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