from src.widget import get_date, mask_account_card
import pytest


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def card():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account():
    return "Счет 73654108430135874305"


def test_widget_date(date):

    assert get_date(date) == "11.03.2024"


def test_widget_number(card, account):

    assert mask_account_card(card) == "Visa Platinum 7000 79** **** 6361"

    assert mask_account_card(account) == "Счет **4305"
