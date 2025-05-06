def mask_account_card(card: str) -> str:
    """Функция которая прячет часть номера карты или счета"""
    from src.masks import get_mask_account, get_mask_card_number
    index = 0
    if card[0] == "С":
        return get_mask_account(card)
    else:
        for i in range(len(card)):
            if card[i].isdigit():
                index = i
                break
        return get_mask_card_number(card, index)


def get_date(date: str) -> str:
    """Функция которая преобразует дату в нужный формат"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
