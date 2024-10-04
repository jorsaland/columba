"""
Namespace for the function that process a request body in order to create an event.
"""


from typing import Any


from app.constants import update_request_valid_fields
from app.repositories.local_sql import EventsRepository
from app.utils.field_validations import catch_invalid_fields


from ._build_update_event_entity import build_update_event_entity


def event_update_from_request_dict(event_id: str, request_dict: dict[str, Any]):

    """
    Process a request body in order to create an event.
    """

    catch_invalid_fields(
        actual_names = request_dict.keys(),
        valid_names = update_request_valid_fields,
    )

    update_event = build_update_event_entity(request_dict)
    return EventsRepository.update_event(event_id, update_event)