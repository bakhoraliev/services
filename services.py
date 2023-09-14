import datetime
from typing import TypedDict

from money import Money


class Service(TypedDict):
    """
    Service is a value object that represents a service that can be
        purchased.
    """

    name: str
    price: Money
    time: datetime.timedelta


__all__ = [
    "Service",
]
