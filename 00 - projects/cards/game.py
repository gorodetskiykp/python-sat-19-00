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
    player_no = 1
    for player, player_cards in players:
        print('Игрок', player_no, '-', player,
              '\nКарты в руке:', *player_cards, '\n')
        player_no += 1


def game():
    players_count = int(input("Укажите количество игроков: "))
    players = get_players(players_count)
    stack = get_stack()
    players = get_cards_for_players(stack, players)
    view_cards(players)



if __name__ == '__main__':
    game()
