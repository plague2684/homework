def get_mask_card_number(number_card: str) -> str:
    """Функция которая прячет часть номера карты"""

    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(account_number: str) -> str:
    """ "Функция которая прячет часть номера счета"""

    return f"**{str(account_number[-4:])}"
