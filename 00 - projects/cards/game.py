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
    while True:
        try:
            players_count = int(input('Укажите кол-во игроков(от 2 до 4):'))
        except ValueError:
            print('Обязательно нужно ввести число от 2 до 4')
            continue
        if players_count in range(2, 4):
            break
        else:
            print('Может быть только от 2 до 4 игроков')
            continue
    players = get_players(players_count)
    stack = get_stack()
    players = get_cards_for_players(stack, players)
    view_cards(players)



if __name__ == '__main__':
    game()
