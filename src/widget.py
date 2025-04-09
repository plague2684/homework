def mask_account_card(card: str) -> str:
    """Функция которая прячет часть номера карты или счета"""

    index = 0
    if card[0] == "С":
        return f"{card[:4]} **{card[-4:]}"
    else:
        for i in range(len(card)):
            if card[i].isdigit():
                index = i
                break
        return f"{card[:index-1]} {card[index:index+4]} {card[index+4:index+6]}** **** {card[-4:]}"
