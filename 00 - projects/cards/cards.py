from random import choice, randint, shuffle
from typing import Optional

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
    Козырь определяется по последней карте в колоде
    В случае пустой колоды - None
    Пример карты - 2♥
    Аргументы:
        stack - список оставшихся после раздачи карт
    Возвращаемое значение:
        Значение масти или None в случае пустой колоды
    """
    if stack:
        return stack[-1][-1]
    return None


def get_minimal_card(hand: list, trump_mark: str = None) -> Optional[str]:
    """Определить минимальную карту у игрока.
    Сначала смотрим не козырные карты, если таких нет -
    отдаём минимальный козырь.

    Аргументы:
        hand - список карт у игрока
        trump_mark - строчное значение козырной масти
    Возвращаемое значение:
        Строчное значение карты
        None
    """
    if not hand:
        return None
    new_hand = []
    for card in hand:
        if trump_mark and trump_mark in card:
            continue
        new_hand.append(card)
    if new_hand:
        new_hand = sorted_cards(new_hand)
    else:
        new_hand = sorted_cards(hand)
    return new_hand[0]


def sorted_cards(unsorted: list) -> list:
    weights = []
    for card in unsorted:
        weights.append(
            (
                cards.index(card[:-1]),
                card,
            )
        )
    return [card for _, card in sorted(weights)]
