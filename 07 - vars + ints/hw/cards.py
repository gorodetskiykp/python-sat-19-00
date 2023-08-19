from random import choice, shuffle, randint

from config import cards, marks, CARDS_LIMIT
from players import get_players


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
    for name, player_cards in players:  #
        need_cards = max(0, CARDS_LIMIT - len(player_cards))
        temporary = get_random_cards(stack, need_cards)
        cards_for_player = [name, temporary + player_cards]
        hands_list.append(cards_for_player)
    return hands_list
