def random_cards() -> list:
    """
    Вернуть перемешанную кололду
    Колода = ['2H', '3H', '4H', '5H', '' ..]
    :param stack:
    :return:
    """
    pass


def get_random_cards(stack: list, count: int) -> list:
    """
    Возвращает первые 'count' элементов из списка 'stack'.

    Args:
        stack (list): Список элементов.
        count (int): Количество элементов, которые нужно вернуть.

    Returns:
        list: Список первых 'count' элементов или пустой список, если 'count' некорректен.
    """
    num_element = len(stack)

    if count > 0 and count < num_element:
        stack = stack[:count]  # Используем срез, чтобы оставить только первые 'count' элементов
        return stack
    else:
        raise ValueError("Вы ввели некорректное число")



def get_cards_for_players(players_names: list) -> list:
    """
    Получает список имен игроков
    Возвращает список списков (по 6 карт)
    [
        ['player1', [карты на руках]],
    ]
    """
    stack = random_cards()  # получить первоначальную колоду
    get_random_cards()  # получить на руки определенное количество карт
