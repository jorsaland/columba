from sqlalchemy import MetaData, insert, select, update


from typing import Any


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

        statement = (
            insert(cls._table)
            .values(**event.as_database_dict())
        )

        with cls._engine.connect() as connection:
            connection.execute(statement)
            connection.commit()


    @classmethod
    def read_all_events(cls):

        with cls._engine.connect() as connection:
            result = connection.execute(select(cls._table))
            events = [Event.from_database_dict({k: v for k, v in zip(ordered_fields, row)}) for row in result.all()]
        
        return events


    @classmethod
    def read_events_by_fields(cls, query: Event):

        statement = select(cls._table)
        for field_name, field_value in query.as_database_dict().items():
            statement = statement.where(getattr(cls._table.c, field_name) == field_value)

        with cls._engine.connect() as connection:
            result = connection.execute(statement)
            events = [Event.from_database_dict({k: v for k, v in zip(ordered_fields, row)}) for row in result.all()]
        
        return events


    @classmethod
    def update_event(cls, event_id: str, updates: Event):

        statement = (
            update(cls._table)
            .where(cls._table.c.event_id == event_id)
            .values(**updates.as_database_dict())
        )

        with cls._engine.connect() as connection:
            connection.execute(statement)
            connection.commit()