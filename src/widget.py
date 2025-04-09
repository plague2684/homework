import masks

def mask_account_card(card: str) -> str:
    """Функция которая прячет часть номера карты или счета"""

    index = 0
    if card[0] == "С":
        return masks.get_mask_account(card)
    else:
        for i in range(len(card)):
            if card[i].isdigit():
                index = i
                break
        return masks.get_mask_card_number(card, index)
