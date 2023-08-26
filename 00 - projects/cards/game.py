from random import randint

from cards import get_cards_for_players, get_stack
from players import get_players


def view_cards(players):
    """
    Вход:
    [
        ['player1', [карты на руках]],
    ]
    Вывести на экран красиво
    """
    for player, player_cards in players:
        print(player, '-', *sorted(player_cards), '\n')


def game():
    players_count = int(input("Укажите количество игроков: "))
    players = get_players(players_count)
    stack = get_stack()
    players = get_cards_for_players(stack, players)
    view_cards(players)



if __name__ == '__main__':
    game()
