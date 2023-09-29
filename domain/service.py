import datetime
from typing import TypedDict

from domain.money import Money


class Service(TypedDict):
    """
    Service is a value object that represents a service that can be
        purchased.

    Contains data about the service, such as its name, description, image URL for cover,
        price, and time it takes to complete the service.
    """

    name: str
    description: str
    image_url: str
    price: Money
    time: datetime.timedelta


__all__ = [
    "Service",
]
