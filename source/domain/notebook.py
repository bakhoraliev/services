from datetime import date, datetime
from typing import TypedDict

from domain.registration import Registration, registration_spent_time


class Notebook(TypedDict):
    """
    Notebook is a value object that represents a notebook of registrations
        for a given day.

    The registrations are sorted by time - from earliest to latest.
    """

    day: date
    registrations: list[Registration]


def day_free_time(notebook: Notebook) -> list[tuple[datetime, datetime]]:
    """
    Calculate the free time intervals for a given day.
    """
    free_time = []
    pointer = datetime.combine(notebook["day"], datetime.min.time())
    for registration in notebook["registrations"]:
        procedures_start = registration["time"]
        procedures_end = registration["time"] + registration_spent_time(
            registration,
        )
        free_time.append((pointer, procedures_start))
        pointer = procedures_end
    free_time.append(
        (pointer, datetime.combine(notebook["day"], datetime.max.time()))
    )
    return free_time


__all__ = [
    "Notebook",
]
