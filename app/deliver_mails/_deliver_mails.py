"""
Defines the function that delivers pending mails.
"""


from datetime import datetime


from app.entities import Event
from app.constants import ACTIVE
from app.response_messages import logger_message_launching_event, logger_message_searching_events
from app.repositories.local_sql import EventsRepository
from app.utils.logger import get_logger


from ._send_mail import send_mail


logger = get_logger()


def deliver_mails():

    """
    Delivers pending mails
    """

    raw_now = datetime.now()
    now = datetime(
        year = raw_now.year,
        month = raw_now.month,
        day = raw_now.day,
        hour = raw_now.hour,
        minute = raw_now.minute,
    )
    logger.debug(logger_message_searching_events.format(time=now))

    filter_event = Event(runtime=now)
    found_events = EventsRepository.select_events_by_filter(filter_event)

    events_to_launch: list[Event] = []
    for event in found_events:

        fields_to_update = Event()

        fields_to_update.runtime = event.runtime + event.period
        if event.state == ACTIVE:
            events_to_launch.append(event)
            fields_to_update.counts = event.counts + 1

        EventsRepository.update_event(event.event_id, fields_to_update)

    for event in events_to_launch:
        logger.info(logger_message_launching_event.format(event_id=event.event_id))
        send_mail(
            sender_name = event.sender_name,
            subject = event.subject,
            is_html = event.is_html,
            message = event.message,
        )