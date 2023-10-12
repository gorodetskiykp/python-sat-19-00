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




