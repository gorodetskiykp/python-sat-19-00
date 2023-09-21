"""Основной модуль игры."""

from random import randint

from cards import (
    get_cards_for_players,
    get_minimal_card,
    get_stack,
    get_trump_card,
    sorted_cards,
)

from players import defence, first_move, get_next_player, get_players, move


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
                and 2 <= (players_count := int(players_count)) <= 4):
            break
        print('Может быть только от 2 до 4 игроков')

    players = get_players(players_count)
    stack = get_stack()
    players = get_cards_for_players(stack, players)
    trump = get_trump_card(stack)
    view_cards(players)
    print('Козырь: {}'.format(trump))
    next_move = first_move(players, trump)
    print('Игру начинает {}'.format(players[next_move][0]))
    next_card = get_minimal_card(players[next_move][-1], trump)
    card_on_desk = move(players[next_move][-1], next_card)
    print('Карта на столе: {}'.format(card_on_desk))
    defender_index = get_next_player(next_move, players_count)
    print('Защищается {}'.format(players[defender_index][0]))
    next_card_to_defend = defence(players[defender_index][-1], next_card, trump)
    if next_card_to_defend is not None:
        print('Игрок {} отбивает картой: {}'.foramt(players[defender_index][0],
                                                    next_card_to_defend))
        card_on_desk = move(players[defender_index][-1], next_card_to_defend)
        print('Карта на столе: {}'.format(card_on_desk))
    else:
        print('Игрок {} не может отбить карту'
              .format(players[defender_index][0]))

    view_cards(players)


def choose_attacking_cards(hand, trump, table_cards=None):
    attacking_cards = []

    if not table_cards:
        minimal_card = get_minimal_card(hand, trump)
        attacking_cards.append(minimal_card)

        def find_pairs_or_threes(hand, count):
            pairs_or_threes = []
            uniq_cards = set(hand)
            for current_card in uniq_cards:
                if hand.count(current_card) >= count and current_card != trump:
                    pairs_or_threes.extend([current_card] * count)
            return pairs_or_threes

        pairs_or_threes = find_pairs_or_threes(hand, 2)
        if pairs_or_threes:
            attacking_cards.append(pairs_or_threes)

        threes = find_pairs_or_threes(hand, 3)
        if threes:
            attacking_cards.append(threes)
    else:
        for card in table_cards:
            if card[0] != trump[0]:
                matching_cards = []
                for current_card in hand:
                    if current_card[0] == card[0]:
                        matching_cards.append(current_card)
                attacking_cards.extend(matching_cards)

    return attacking_cards



if __name__ == '__main__':
    game()
