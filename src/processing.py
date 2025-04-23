def filter_by_state(info: list[dict], state="EXECUTED") -> list[dict]:
    """Функция которая возвращяет только те значения, которые подходят под критерий"""
    answer = []
    for i in info:
        if i["state"] == state:
            answer.append(i)

    return answer


def sort_by_date(info: list[dict], reversed=False) -> list[dict]:
    """Функция которая сортирует по дате"""
    answer = sorted(info, key=lambda s: s["date"], reverse=reversed)

    return answer
