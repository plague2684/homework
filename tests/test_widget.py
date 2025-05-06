from src.widget import get_date, mask_account_card
import pytest


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


def test_widget_date(date):

    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize('value, answer', [
    ('Visa Platinum 7000792289606361', "Visa Platinum 7000 79** **** 6361"),
    ('Счет 73654108430135874305', "Счет **4305")
])


def test_widget_number(value, answer):

    assert mask_account_card(value) == answer

