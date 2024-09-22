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
)


@dataclass
class Event:


    """
    Represents events.
    """

    event_id: str = None
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
        if self.first_runtime is not None:
            database_dict[FIELD_NAME_FIRST_RUNTIME] = self.first_runtime.isoformat()
        if self.next_runtime is not None:
            database_dict[FIELD_NAME_NEXT_RUNTIME] = self.next_runtime.isoformat()
        if self.message is not None:
            database_dict[FIELD_NAME_MESSAGE] = self.message
        if self.period is not None:
            database_dict[FIELD_NAME_PERIOD] = int(self.period.total_seconds())

        return database_dict
    

    @classmethod
    def from_database_dict(cls, database_dict: dict[str, Any]):

        """
        Builds an event from the format used by the database.
        """

        event = Event(**{
            FIELD_NAME_EVENT_ID: database_dict[FIELD_NAME_EVENT_ID],
            FIELD_NAME_FIRST_RUNTIME: datetime.fromisoformat(database_dict[FIELD_NAME_FIRST_RUNTIME]),
            FIELD_NAME_NEXT_RUNTIME: datetime.fromisoformat(database_dict[FIELD_NAME_NEXT_RUNTIME]),
            FIELD_NAME_MESSAGE: database_dict[FIELD_NAME_MESSAGE],
            FIELD_NAME_PERIOD: timedelta(seconds=database_dict[FIELD_NAME_PERIOD]),
        })

        return event