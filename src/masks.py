def get_mask_card_number(number_card: str, index: int) -> str:
    """Функция которая прячет часть номера карты"""

    return f"{number_card[:index-1]} {number_card[index:index+4]} {number_card[index+4:index+6]}** **** {number_card[-4:]}"


def get_mask_account(account_number: str) -> str:
    """ "Функция которая прячет часть номера счета"""

    return f"{account_number[:4]} **{account_number[-4:]}"
