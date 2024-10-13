"""
Defines the function that gets the SQL table of events.
"""


from sqlalchemy import MetaData, Table, Column, INTEGER, VARCHAR, TEXT, BOOLEAN


from app.constants import (
    TABLE_NAME_EVENTS,
    FIELD_COUNTS,
    FIELD_RUNTIME,
    FIELD_EVENT_ID,
    FIELD_MESSAGE,
    FIELD_SENDER_NAME,
    FIELD_IS_HTML,
    FIELD_SUBJECT,
    FIELD_PERIOD,
    FIELD_STATE,
)


def get_events_table(metadata: MetaData):

    """
    Gets the SQL table of events.
    """

    return Table(

        TABLE_NAME_EVENTS, metadata,

        Column(FIELD_EVENT_ID, VARCHAR),
        Column(FIELD_STATE, VARCHAR),
        Column(FIELD_COUNTS, INTEGER),

        Column(FIELD_RUNTIME, VARCHAR),
        Column(FIELD_PERIOD, INTEGER),

        Column(FIELD_SENDER_NAME, TEXT),
        Column(FIELD_SUBJECT, TEXT),
        Column(FIELD_IS_HTML, BOOLEAN),
        Column(FIELD_MESSAGE, TEXT),
    )