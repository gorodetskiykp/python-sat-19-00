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
    Принимает оставшуюся кололду
    Возвращает указанное количество карт
    """


def get_cards_for_players(players_names: list) -> list:
    """
    Получает список имен игроков
    Возвращает список списков (по 6 карт)
    [
        ['player1', [карты на руках]],
    ]
    """
    stack = random_cards() # получить первоначальную колоду
    get_random_cards() # получить на руки определенное количество карт
