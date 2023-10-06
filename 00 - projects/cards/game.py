"""Основной модуль игры."""

from random import randint

from cards import (
    choose_attacking_cards,
    defence,
    get_cards_for_players,
    get_minimal_card,
    get_stack,
    get_trump_card,
    move,
    sorted_cards,
)
from config import max_count_of_players, min_count_of_players

from players import first_move, get_next_player, get_players


def view_cards(players) -> None:
    """Напечатать карты игроков (вывести на экран красиво).

    Args:
        players: список игроков
            [
                ['player1', [карты на руках]],
                ['player2', [карты на руках]],
            ]
    Returns:
        None
    """
    for player, player_cards in players:
        print(player, '-', *sorted_cards(player_cards))


def game():
    """Играть в карты."""
    while True:
        players_count = input('Сколько будет игроков? ')
        if (players_count.isdigit()
                and min_count_of_players <=
                (players_count := int(players_count)) <= max_count_of_players):
            break
        print('Может быть только от 2 до 4 игроков')

    players = get_players(players_count)
    stack = get_stack()
    players = get_cards_for_players(stack, players)
    trump = get_trump_card(stack, players)
    view_cards(players)
    print('Козырь: {}'.format(trump))
    next_move = first_move(players, trump)
    print('Игру начинает {}'.format(players[next_move][0]))
    cards_on_desk = choose_attacking_cards(players[next_move][-1], trump, stack)
    print('Карты на столе: {}'.format(', '.join(cards_on_desk)))
    defender_index = get_next_player(next_move, players_count)
    print('Защищается {}'.format(players[defender_index][0]))
    cards_to_defend = defence(players[defender_index][-1], cards_on_desk, trump)
    # если атакующих карт больше, чем карт на руке
    # и смог потратить все свои карты
    # вернуть какой-то признак, чтобы атакующий забрал свои небитые карты
    if cards_to_defend is not None:
        print('Игрок {} отбивает: {}'.format(players[defender_index][0],
                                             cards_to_defend))
        cards_on_desk = choose_attacking_cards(players[next_move][-1], trump,
                                               stack, cards_to_defend)
        print(cards_on_desk)
    else:
        print('Игрок {} не может отбить карту'
              .format(players[defender_index][0]))

    view_cards(players)
    players = get_cards_for_players(stack, players)     
    view_cards(players)

if __name__ == '__main__':
    game()
