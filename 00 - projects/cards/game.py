from random import randint

from cards import (
    get_cards_for_players,
    get_minimal_card,
    get_stack,
    get_trump_card
)
from players import get_players, move


def view_cards(players):
    """
    Вход:
    [
        ['player1', [карты на руках]],
        ['player2', [карты на руках]],
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
        players_count = input('Сколько будет игроков? ')
        if (players_count.isdigit()
                and 2 <= (players_count := int(players_count)) <= 4):
            break
        print('Может быть только от 2 до 4 игроков')

    players = get_players(players_count)
    stack = get_stack()
    players = get_cards_for_players(stack, players)
    trump = get_trump_card(stack)
    if not trump:
        trump = players[-1][-1][-1][-1]
    view_cards(players)
    print('Козырь:', trump)
    first_move = 0
    next_card = get_minimal_card(players[first_move][-1], trump)
    card_on_desk = move(players[first_move][-1], next_card)
    print('Карта на столе:', card_on_desk)
    view_cards(players)

if __name__ == '__main__':
    game()
