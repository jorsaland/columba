from sqlalchemy import MetaData, insert, select, update, delete


from typing import Any


from app.constants import ordered_fields, substring_query_fields
from app.entities import Event
from app.internal_messages import response_message_not_found
from app.utils.exceptions import ValidationError


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
    def insert_event(cls, event: Event):

        """
        Creates an event.
        """

        statement = (
            insert(cls._table)
            .values(**event.as_database_dict())
        )

        with cls._engine.connect() as connection:
            connection.execute(statement)
            connection.commit()
        
        return cls.select_event_by_id(event.event_id)


    @classmethod
    def select_all_events(cls):

        """
        Selects all the events.
        """

        with cls._engine.connect() as connection:
            result = connection.execute(select(cls._table))
            events = [Event.from_database_dict({k: v for k, v in zip(ordered_fields, row)}) for row in result.all()]
        
        return events


    @classmethod
    def select_event_by_id(cls, event_id: str):

        """
        Selects a single event by ID.
        """

        statement = (
            select(cls._table)
            .where(cls._table.c.event_id == event_id)
        )

        with cls._engine.connect() as connection:
            result = connection.execute(statement)
            event_matches = [Event.from_database_dict({k: v for k, v in zip(ordered_fields, row)}) for row in result.all()]

        if not event_matches:
            raise ValidationError(code=404, message=response_message_not_found)

        return event_matches[0]


    @classmethod
    def select_events_by_filter(cls, filters: Event):

        """
        Selects multiple filtered events.
        """

        statement = select(cls._table)
        for field_name, field_value in filters.as_database_dict().items():
            if field_name in substring_query_fields:
                statement = statement.where(getattr(cls._table.c, field_name).like(f'%{field_value}%'))
            else:
                statement = statement.where(getattr(cls._table.c, field_name) == field_value)

        with cls._engine.connect() as connection:
            result = connection.execute(statement)
            events = [Event.from_database_dict({k: v for k, v in zip(ordered_fields, row)}) for row in result.all()]
        
        return events


    @classmethod
    def update_event(cls, event_id: str, updates: Event):

        """
        Updates a single event by ID.
        """

        cls.select_event_by_id(event_id)

        statement = (
            update(cls._table)
            .where(cls._table.c.event_id == event_id)
            .values(**updates.as_database_dict())
        )

        with cls._engine.connect() as connection:
            connection.execute(statement)
            connection.commit()
        
        return cls.select_event_by_id(event_id)


    @classmethod
    def delete_event(cls, event_id: str):

        """
        Deletes a single event by ID.
        """

        event = cls.select_event_by_id(event_id)

        statement = (
            delete(cls._table)
            .where(cls._table.c.event_id == event_id)
        )

        with cls._engine.connect() as connection:
            connection.execute(statement)
            connection.commit()
        
        return event