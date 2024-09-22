"""
Defines the function that gets the SQL table of events.
"""


from sqlalchemy import MetaData, Table, Column, INTEGER, VARCHAR, TEXT


from app.constants import (
    TABLE_NAME_EVENTS,
    FIELD_NAME_FIRST_RUNTIME,
    FIELD_NAME_NEXT_RUNTIME,
    FIELD_NAME_EVENT_ID,
    FIELD_NAME_MESSAGE,
    FIELD_NAME_PERIOD,
)


def get_events_table(metadata: MetaData):

    """
    Gets the SQL table of events.
    """

    return Table(
        TABLE_NAME_EVENTS, metadata,
        Column(FIELD_NAME_EVENT_ID, VARCHAR),
        Column(FIELD_NAME_FIRST_RUNTIME, VARCHAR),
        Column(FIELD_NAME_NEXT_RUNTIME, VARCHAR),
        Column(FIELD_NAME_MESSAGE, TEXT),
        Column(FIELD_NAME_PERIOD, INTEGER),
    )