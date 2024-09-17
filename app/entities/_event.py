"""
Defines the class that represents events.
"""


from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Event:

    """
    Represents events.
    """

    first_runtime: datetime
    next_runtime: datetime
    message: str
    period: timedelta