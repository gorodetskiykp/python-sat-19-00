import pytest

import cards


def random_cards() -> list:
    return [card for cards in range(36)]


def test_get_cards_for_players():
    players_names = ['Bob', 'John']
    players_cards = cards.get_cards_for_players(players_names)
    assert type(players_cards) == list
    assert len(players_cards) == len(players_names)