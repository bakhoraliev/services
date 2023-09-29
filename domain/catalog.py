from typing import TypedDict

from domain.service import Service


class Category(TypedDict):
    """Category is a value object that represents a category of services."""

    name: str
    services: list[Service]


class Catalog(TypedDict):
    """Catalog is a value object that represents a catalog of services."""

    categories: list[Category]


__all__ = [
    "Catalog",
    "Category",
]
