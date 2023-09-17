"""Обработка игроков."""

from typing import Optional

from config import black_list, cards
from cards import get_minimal_card, sorted_cards


def get_players(players_count: int) -> list:
    players = []
    players_names = []
    while len(players) < players_count:
        name = input('Введите имя игрока: ').strip()
        if len(name) < 3:
            print('Имя должно содержать минимум 3 символа. Попробуйте ещё раз')
        elif name in black_list:
            print('Игрок в чёрном списке')
        elif name in players_names:
            print('Такой игрок уже есть')
        else:
            players.append([name, []])
            players_names.append(name)
    return players


def first_move(players: list, trump_mark: str) -> int:
    """Определить игрока, который начнёт игру.
    Нужно проверить карты игроков и найти минимальный козырь
    Если ни у кого нет козырей, ходит игрок № 0

    Аргументы:
        players - список игроков и из карт
            [
                ['p1', ['k1', 'k2', ...]],
                ['p2', ['k1', 'k2', ...]],
            ]
        trump_mark - строчное значение козырной масти
    Возвращаемое значение:
        Порядковый номер игрока, который начинает игру
    """
    tramp_cards = []
    for _, cards in players:
        for card in cards:
            if trump_mark in card:
                tramp_cards.append(card)
    player_no = 0
    if tramp_cards:
        min_tramp_card = get_minimal_card(tramp_cards)
        for _, cards in players:
            if min_tramp_card in cards:
                return player_no
            player_no += 1
    return 0


def get_next_player(current_player_index: int, players_count: int):
    """Определить индекс следующего игрока."""
    return (current_player_index + 1) % players_count


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


def defence(hand: list, attacking_cards: list,
            trump_suit: str) -> Optional[dict]:
    """Определить карту для защиты.

    Если на столе несколько карт - нужно найти, чем отбить их все.

    Args:
        hand: list
            список карт на руках у защищающегося игрока.
        attacking_cards: list
            карты на столе, которые нужно отбить.
        trump_suit: str
            козырная масть.
    Returns:
        - Карты, которыми можно отбить
        - None, если отбить нечем
    """
    trump_cards = []
    defence_cards = {}
    for hand_card in hand:
        if trump_suit in hand_card:
            trump_cards.append(hand_card)
    for attacking_card in attacking_cards:
        same_suit_cards = []
        for hand_card in hand:
            if (hand_card not in defence_cards.values()
                    and attacking_card[-1] in hand_card):
                same_suit_cards.append(hand_card)
        for defence_card in sorted_cards(same_suit_cards):
            if (cards.index(defence_card[:-1])
                    > cards.index(attacking_card[:-1])):
                defence_cards[attacking_card] = defence_card
                break
        else:
            defence_card = get_minimal_card(trump_cards)
            if defence_card:
                defence_cards[attacking_card] = defence_card
                trump_cards.remove(defence_card)
            else:
                hand.extend(attacking_cards)
                return None
    for card in defence_cards.values():
        move(hand, card)
    return defence_cards
