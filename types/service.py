import datetime
from typing import TypedDict

from types.money import Money


class Service(TypedDict):
    """
    Service is a value object that represents a service that can be
        purchased.

    Contains data about the service, such as its name, description, image URL for cover,
        price, and time it takes to complete the service and its options.
    """

    name: str
    description: str
    image_url: str
    price: Money
    time: datetime.timedelta
    options: list["Option"]


class Option(TypedDict):
    """
    Option is a value object that represents an option for a service.
    """

    name: str
    description: str
    image_url: str
    price_diff: Money
    time_diff: datetime.timedelta


__all__ = [
    "Service",
    "Option",
]
