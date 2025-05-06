import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def date() -> str:
    """Дата для проверки"""
    return "2024-03-11T02:26:18.671407"


def test_widget_date(date: str) -> None:
    """Проверка роботоспособности перевода даты"""

    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize(
    "value, answer",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_widget_number(value: str, answer: str) -> None:
    """Проверка роботоспособности скрытия номера"""

    assert mask_account_card(value) == answer
