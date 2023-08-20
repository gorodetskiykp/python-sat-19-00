from players import get_players
from cards import get_cards_for_players
from random import randint


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
    players_names = get_players(players_count)
    players_cards = get_cards_for_players(players_names)
    view_cards(players_cards)


if __name__ == '__main__':
    game()
