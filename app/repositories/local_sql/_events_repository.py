from sqlalchemy import MetaData, insert, select, update


from app.constants import ordered_fields
from app.entities import Event


from ._get_engine import get_engine
from ._get_events_table import get_events_table


class EventsRepository:


    """
    Connects to SQL local database and performs CRUD operations.
    """


    _metadata = MetaData()
    _table = get_events_table(_metadata)
    _engine = get_engine()


    @classmethod
    def create_event(cls, event: Event):

        with cls._engine.connect() as connection:
            connection.execute(
                insert(cls._table)
                .values(**event.as_database_dict())
            )
            connection.commit()


    @classmethod
    def read_all_events(cls):

        with cls._engine.connect() as connection:
            result = connection.execute(select(cls._table))
            events = [Event.from_database_dict({k: v for k, v in zip(ordered_fields, row)}) for row in result.all()]
            return events


    @classmethod
    def update_event(cls, event_id: str, event: Event):

        with cls._engine.connect() as connection:
            connection.execute(
                update(cls._table)
                .where(cls._table.c.event_id == event_id)
                .values(**event.as_database_dict())
            )
            connection.commit()