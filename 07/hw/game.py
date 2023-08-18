from players import get_players
from cards import get_cards_for_players
from random import randint

def view_cards(players_cards):
    """
    Вход:
    [
        ['player1', [карты на руках]],
    ]
    Вывести на экран красиво
    """
    for player in range(len(players_cards)):
        for cards in range(6):
            card = players_cards[player][1][cards]
            if 'H' in card:
                card = card.replace('H', '♥')
            elif 'D' in card:
                card = card.replace('D', '♦')
            elif 'C' in card:
                card = card.replace('C', '♣')
            elif 'S' in card:
                card = card.replace('S', '♠')
            players_cards[player][1][cards] = card
        print('Игрок', player + 1, '-', players_cards[player][0],
              '\nКарты в руке:', *players_cards[player][1], '\n')
    egg = randint(1, 100)  # пасхалка
    if egg > 90:
        print('Все игроки - пусечки!')


def game():
    players_count = int(input("Укажите количество игроков: "))
    players_names = get_players(players_count)
    players_cards = get_cards_for_players(players_names)
    view_cards(players_cards)
