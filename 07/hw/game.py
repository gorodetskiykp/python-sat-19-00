from players import get_players
from cards import get_cards_for_players

def view_cards(players_cards):
    """
    Вход:
    [
        ['player1', [карты на руках]],
    ]
    Вывести на экран красиво
    """

def game():
    players_count = int(input("Укажите количество игроков: "))
    players_names = get_players(players_count)
    players_cards = get_cards_for_players(players_names)
    view_cards(players_cards)
