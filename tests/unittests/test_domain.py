from decimal import Decimal

import pytest

from domain.money import Money


@pytest.mark.parametrize(
    "amount, rounded_up_amount",
    [
        (Decimal("1.234"), Decimal("1.23")),
        (Decimal("1.235"), Decimal("1.24")),
        (Decimal("1.236"), Decimal("1.24")),
    ],
)
def test_money_amount_round_up(amount: Decimal, rounded_up_amount: Decimal):
    """Test that the amount is rounded up to 2 decimal places."""
    money = Money(amount=amount, currency="USD")

    assert money.amount == rounded_up_amount
