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
    get_next_player
)

from players import first_move, get_players


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
    for player_name, player_cards in players:
        print(player_name, '-', *sorted_cards(player_cards))


def game():
    """Играть в карты."""
    # while True:
    #     players_count = input('Сколько будет игроков? ')
    #     if (players_count.isdigit()
    #             and 2 <= (players_count := int(players_count)) <= 4):
    #         break
    #     print('Может быть только от 2 до 4 игроков')
    #
    # players = get_players(players_count)
    players_count = 5
    players = [
        ["Player1", []],
        ["Player2", []],
        ["Player3", []],
        ["Player4", []],
        ["Player5", []],
    ]
    stack = get_stack()
    players = get_cards_for_players(stack, players)
    trump = get_trump_card(stack, players)
    view_cards(players)
    print('Козырь: {}'.format(trump))
    # while True:
    next_move = first_move(players, trump)
    print('Атакует {}'.format(players[next_move][0]))
    defender_index = get_next_player(next_move, players_count)
    print('Защищается {}'.format(players[defender_index][0]))
    cards_on_desk = {}
    while True:
        cards_on_desk = choose_attacking_cards(players[next_move][-1], trump,
                                               stack, cards_on_desk)
        if cards_on_desk is None:
            print('Переходим к следующему игроку')
            break
        print('Карты на столе: {}'.format(', '.join(cards_on_desk)))  # пока выводит только ключи, нужно добавить и значения
        cards_on_desk = defence(players[defender_index][-1], cards_on_desk, trump)
        # если атакующих карт больше, чем карт на руке
        # и смог потратить все свои карты
        # вернуть какой-то признак, чтобы атакующий забрал свои небитые карты
        if cards_on_desk is None:
            print('Игрок {} не может отбить карты'
                  .format(players[defender_index][0]))
            break
        else:
            print('Игрок {} отбивает: {}'.format(players[defender_index][0],
                                                 cards_on_desk))
        view_cards(players)


    players = get_cards_for_players(stack, players, next_move)
    view_cards(players)



if __name__ == '__main__':
    game()
