from datetime import datetime, timedelta
from typing import TypedDict

from services import Service


class Registration(TypedDict):
    """
    Registration is a value object that represents a registration for
        services.
    """

    name: str
    phone: str
    services: list[Service]
    time: datetime


def registration_spent_time(registration: Registration) -> timedelta:
    """
    Calculate the total time spent on all services in a registration.
    """
    total = timedelta()
    for service in registration["services"]:
        total += service["time"]
    return total


__all__ = [
    "Registration",
]
