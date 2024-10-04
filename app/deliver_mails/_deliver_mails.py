"""
Defines the function that delivers pending mails.
"""


from datetime import datetime


from app.entities import Event
from app.constants import ACTIVE
from app.repositories.local_sql import EventsRepository


from ._send_mail import send_mail


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

    messages: list[str] = []
    filter_event = Event(next_runtime=now)

    for event in EventsRepository.select_events_by_filter(filter_event):

        if event.state == ACTIVE:
            messages.append(event.message)

        if event.period.total_seconds() > 0:
            next_runtime = event.next_runtime + event.period
            fields_to_update = Event(next_runtime=next_runtime)
            EventsRepository.update_event(event.event_id, fields_to_update)

    for message in messages:
        send_mail(message)