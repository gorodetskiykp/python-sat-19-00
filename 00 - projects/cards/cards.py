from random import choice, randint, shuffle

from config import cards, CARDS_LIMIT, marks


def get_stack() -> list:
    """
    Вернуть перемешанную колоду
    """
    stack = []
    for card in cards:
        for mark in marks:
            stack.append(card + mark)
    shuffle(stack)
    return stack


def get_random_cards(stack: list, count: int) -> list:
    """
    Принимает оставшуюся колоду
    Возвращает указанное количество карт
    """
    hand = []
    for _ in range(count):
        card = choice(stack)
        hand.append(card)
        stack.remove(card)
    return hand


def get_cards_for_players(stack: list, players: list) -> list:
    """
    Получает список имен игроков
    Возвращает список списков (по 6 карт)
    [
        ['player1', [карты на руках]],
    ]
    """
    hands_list = []
    for name, player_cards in players:
        need_cards = max(0, CARDS_LIMIT - len(player_cards))
        temporary = get_random_cards(stack, need_cards)
        cards_for_player = [name, temporary + player_cards]
        hands_list.append(cards_for_player)
    return hands_list


def get_trump_card(stack: list):
    """Определить козырь.
    Козырь положить под низ колоды

    Аргументы:
        stack - список оставшихся после раздачи карт
    Возвращаемое значение:
        Значение масти

    Козырь определяется по последней карте в перемешанной колоде
    В случае пустой колоды - None
    """
    if len(stack) > 0:
        return stack[-1][-1]
    else:
        return None


def get_minimal_card(hand: list, tramp_mark: str) -> str:
    """Определить минимальную не козырную карту у игрока.

    Аргументы:
        hand - список карт у игрока
        tramp_mark - строчное значение козырной масти
    Возвращаемое значение:
        Строчное значение карты
    """
