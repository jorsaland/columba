"""
Namespace for the function that reads all events or filter them by query parameters.
"""


from app.constants import valid_query_params
from app.repositories.local_sql import EventsRepository
from app.utils.field_validations import catch_invalid_query_params
import switches


from ._build_filter_event_entity import build_filter_event_entity


def events_read_from_query_params(query_params: dict[str, str]):

    """
    Reads all events or filter them by query parameters.
    """

    if not query_params:
        found_events = EventsRepository.select_all_events()

    else:

        if switches.REJECT_INVALID_QUERY_PARAMS:
            catch_invalid_query_params(query_params=query_params, valid_names=valid_query_params)

        filter_event = build_filter_event_entity(query_params)
        found_events = EventsRepository.select_events_by_filter(filter_event)

    return found_events