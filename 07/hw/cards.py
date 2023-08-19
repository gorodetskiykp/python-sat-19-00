from players import get_players
from random import shuffle
from random import choice


def random_cards() -> list:
    """
    Вернуть перемешанную колоду
    Колода = ['2H', '3H', '4H', '5H', '' ..]
    :param stack:
    :return:
    """
    stack = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH',
            'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S',
            'JS', 'QS', 'KS', 'AS', '2D', '3D', '4D', '5D', '6D', '7D', '8D',
            '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2C', '3C', '4C', '5C', '6C',
            '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC']
    shuffle(stack)
    return stack


def get_random_cards(stack: list, count: int) -> list:
    """
    Принимает оставшуюся колоду
    Возвращает указанное количество карт
    """
    hand = []
    for drop in range(count):
        card = choice(stack)
        hand.append(card)
        stack.remove(card)
    return hand


def get_cards_for_players(players_names: list) -> list:
    """
    Получает список имен игроков
    Возвращает список списков (по 6 карт)
    [
        ['player1', [карты на руках]],
    ]
    """
    hands_list = []
    stack = random_cards()  # получить первоначальную колоду
    for name in players_names:  #
        temporary = get_random_cards(stack, 6)
        cards_for_player = [players_names[name], [temporary]]
        hands_list.append(cards_for_player)
        for card in temporary:
            stack.remove(temporary[card])
    return hands_list
