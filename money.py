from decimal import Decimal

from pydantic import BaseModel, validator


class Money(BaseModel):
    """Money is a value object that represents a monetary amount."""

    amount: Decimal
    currency: str

    @validator("amount")
    def round_up_amount(cls, value: Decimal) -> Decimal:
        return value.quantize(Decimal("0.01"))

    class Config:
        json_encoders = {
            Decimal: lambda v: str(v),
        }
        frozen = True


__all__ = [
    "Money",
]
