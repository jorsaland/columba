"""
Defines the function that gets the SQL table of events.
"""


from sqlalchemy import MetaData, Table, Column, INTEGER, VARCHAR, TEXT


def get_events_table(metadata: MetaData):

    """
    Gets the SQL table of events.
    """

    return Table(
        'Events', metadata,
        Column('first_runtime', VARCHAR),
        Column('next_runtime', VARCHAR),
        Column('message', TEXT),
        Column('period', INTEGER),
    )