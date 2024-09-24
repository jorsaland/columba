"""
Namespace for the function that process a request body in order to create an event.
"""


from typing import Any


from app.constants import creation_request_valid_fields, creation_request_mandatory_fields
from app.repositories.local_sql import EventsRepository
from app.utils.field_validations import catch_invalid_fields, catch_missing_required_fields


from ._build_creation_event_entity import build_event_creation_entity


def event_create_from_request_dict(request_dict: dict[str, Any]):

    """
    Process a request body in order to create an event.
    """

    # Validate request structure

    catch_invalid_fields(
        actual_names = request_dict.keys(),
        valid_names = creation_request_valid_fields,
    )

    catch_missing_required_fields(
        request_dict = request_dict,
        required_names = creation_request_mandatory_fields,
    )

    # Validate and convert values

    event_to_create = build_event_creation_entity(request_dict)
    return EventsRepository.create_event(event_to_create)