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
        return f"{card[:i-1]} {card[i:i+4]} {card[i+4:i+6]}** **** {card[-4:]}"

print(mask_account_card("Visa Platinum 8990922113665229"))