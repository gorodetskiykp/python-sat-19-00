"""Обработка колоды / карт."""

from random import choice, shuffle
from typing import Optional

from config import cards, CARDS_LIMIT, marks


def get_stack() -> list:
    """Вернуть перемешанную колоду."""
    stack = []
    for card in cards:
        for mark in marks:
            stack.append(card + mark)
    shuffle(stack)
    return stack


def get_random_cards(stack: list, count: int) -> list:
    """Вернуть указанное количество карт из колоды."""
    hand = []
    for _ in range(count):
        card = choice(stack)
        hand.append(card)
        stack.remove(card)
    return hand


def get_cards_for_players(stack: list, players: list) -> list:
    """Раздать карты игрокам.

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


def get_trump_card(stack: list, players: list) -> str:
    """Определить козырь.

    Козырь определяется по последней карте в колоде
    В случае пустой колоды берем последнюю карту последнего игрока
    Пример масти - ♥
    Аргументы:
        stack - список оставшихся после раздачи карт
        players - списко игроков
    Возвращаемое значение:
        Значение масти, которая будет козырем
    """
    if stack:
        return stack[-1][-1]
    return players[-1][-1][-1][-1]


def get_card_value(card: str) -> str:
    """Получить номинал карты

    Аргументы:
        card - строчное значение карты

    Возвращаемое значение:
        Строчное значение номинала
    """
    return card[:-1]

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
    """Отсортировать карты по номиналу.

    Args:
        unsorted: list
            список карт, которые нужно отсортировать

    Returns:
        - Список отсортированных карт
    """
    weights = []
    for unsorted_card in unsorted:
        weights.append(
            (
                cards.index(get_card_value(unsorted_card)),
                unsorted_card,
            ),
        )
    return [card for _, card in sorted(weights)]


def get_minimal_similar_cards(hand, tramp, stack):
    similar_cards = dict.fromkeys(cards)
    hand_cards = hand[:]
    if stack:
        hand_cards = [card for card in hand_cards if tramp not in card]
    for card in hand_cards:
        value = get_card_value(card)
        if similar_cards[value]:
            similar_cards[value].append(card)
        else:
            similar_cards[value] = [card]
    similar_cards = {value: cards for value, cards in similar_cards.items()
                     if cards and len(cards) > 1}
    result = []
    for value in cards:
        if len(similar_cards.get(value, [])) == 2:
            result.append(similar_cards.get(value))
            break
    for value in cards:
        if len(similar_cards.get(value, [])) == 3:
            result.append(similar_cards.get(value))
            break
    return result


def choose_attacking_cards(hand: list, trump: str, stack: list,
                           table_cards: dict = None) -> dict:
    """Вернуть на стол карты для атаки.

    Args:
        hand: list
        trump: str
        stack: list
        table_cards: dict = None
    Returns:
        table_cards: dict
    """
    attacking_cards = []

    if not table_cards:
        attacking_cards = choice([
            [get_minimal_card(hand, trump)],
            *get_minimal_similar_cards(hand, trump, stack)
        ])
        for card in attacking_cards:
            move(hand, card)
        return dict.fromkeys(attacking_cards)

    table_cards_list = list(table_cards.keys()) + list(table_cards.values())
    table_cards_list = set([get_card_value(card) for card in table_cards_list])
    for card_value in table_cards_list:
        matching_cards = []
        for hand_card in hand:
            if card_value in hand_card:
                if stack and trump in hand_card:
                    continue
                matching_cards.append(hand_card)
        attacking_cards.extend(matching_cards)
    for card in attacking_cards:
        move(hand, card)
    table_cards.update(dict.fromkeys(attacking_cards))
    return table_cards


def move(hand: list, card: str):
    """Убрать карту из карт игрока.

    Аргументы:
        hand - список карт у игрока
        card - строчное значение карты, которую нужно выложить на стол
    Возвращаемое значение:
        Строчное значение карты
    """
    hand.remove(card)
    return card


def defence(hand: list, attacking_cards: dict,
            trump_suit: str) -> Optional[dict]:
    """Определить карту для защиты.

    Если на столе несколько карт - нужно найти, чем отбить их все.

    Args:
        hand: list
            список карт на руках у защищающегося игрока.
        attacking_cards: dict
            карты на столе, которые нужно отбить.
            это словарь, если есть значение, значит карта уже была отбита.
        trump_suit: str
            козырная масть.
    Returns:
        - Карты, которыми можно отбить
        - None, если отбить нечем
    """
    # если атакующих карт больше, чем карт на руке
    # и смог потратить все свои карты
    # вернуть какой-то признак, чтобы атакующий забрал свои небитые карты

    #!!! переделать алгоритм поиска карты, которую нужно отбить,
    # если атакующих карт больше, чем карт на руке

    #!!! Если не смогли отбить, нужно взять только такое количество атакующих карт,
    # сколько карт на руке (самые маленькие)
    trump_cards = []
    defence_cards = {}
    for hand_card in hand:
        if trump_suit in hand_card:
            trump_cards.append(hand_card)
    attacking_cards_list = [attacking_card
                            for attacking_card, defending_card
                            in attacking_cards.items() if not defending_card]
    for attacking_card in attacking_cards_list:
        same_suit_cards = []
        for hand_card in hand:
            if (hand_card not in defence_cards.values()
                    and get_card_value(attacking_card) in hand_card):
                same_suit_cards.append(hand_card)
        for defence_card in sorted_cards(same_suit_cards):
            if (cards.index(get_card_value(defence_card))
                    > cards.index(get_card_value(attacking_card))):
                defence_cards[attacking_card] = defence_card
                break
        else:
            defence_card = get_minimal_card(trump_cards)
            if defence_card:
                defence_cards[attacking_card] = defence_card
                trump_cards.remove(defence_card)
            else:
                hand.extend(attacking_cards.keys())
                return None
    for card in defence_cards.values():
        move(hand, card)
    return defence_cards  # TODO нужно возвращать все карты со стола
