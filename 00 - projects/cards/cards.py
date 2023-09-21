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
                cards.index(unsorted_card[:-1]),
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
        value = card[:-1]
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
                           table_cards: dict = None) -> list:
    # Аргументы:
    #
    # карты ну руке атакующего
    # козырь
    # карты на столе (необязательный)
    # stack
    # Когда карт на столе нет:
    #
    # сначала ищем карту с помощью get_minimal_card
    # потом ищем пары/тройки одинаковых карт (без козыря) - оформить в отдельную функцию
    # из этих вариантов ходим рандомом [[7], [9, 9], [8, 8, 8]]
    # Если карты на столе есть:
    #
    # выкидываем все карты на стол (кроме козырей), которые подходят по номиналам
    #
    # Если колода пустая
    #
    # не смотрим на козыри - если есть что выкинуть - выкидываем
    # !!! Если атаковал, то внутри функции нужно удалить карты из hand (с помощью move())
    attacking_cards = []

    if not table_cards:
        # пока убрать return - нам нужно карты из choice удалить из руки
        return choice([
            [get_minimal_card(hand, trump)],
            *get_pairs_or_threes(hand)
        ])

    # list(a.keys()) + list(a.values())
    # взять из всех значений только номиналы
    # список значений - удалить дубликаты = table_cards
    #
    #
    #
    for card in table_cards:
        if card[-1] != trump:  # это лишнее - нам все равно, что на столе лежит козырь
            matching_cards = []
            for current_card in hand:  # если стэк не пустой козыри не отдавать
                if current_card[:-1] == card[:-1]:
                    matching_cards.append(current_card)
            attacking_cards.extend(matching_cards)

    return attacking_cards
