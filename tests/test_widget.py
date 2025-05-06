import pytest
from src.widget import get_date


def test_widget_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

def test_widget_number():
    assert mask_account_card("7000792289606361") == "7000 79** **** 6361"