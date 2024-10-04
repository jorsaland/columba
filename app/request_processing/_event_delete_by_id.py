"""
Namespace for the function that deletes an event by ID.
"""


from app.repositories.local_sql import EventsRepository


def event_delete_by_id(event_id: str):

    """
    Deletes an event by ID.
    """

    return EventsRepository.delete_event(event_id)