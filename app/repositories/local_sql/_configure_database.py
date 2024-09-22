"""
Defines the function that configures tables metadata.
"""


from sqlalchemy import MetaData


from ._get_engine import get_engine
from ._get_events_table import get_events_table


def configure_database():

    """
    Configures tables metadata.
    """

    engine = get_engine()
    metadata = MetaData()

    get_events_table(metadata)
    metadata.create_all(engine)