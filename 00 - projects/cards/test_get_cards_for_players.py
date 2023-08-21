from cards import get_cards_for_players, get_stack

players = [['p1', ['2♥']], ['p2', []]]
assert isinstance(get_cards_for_players(get_stack(), players), list)
assert len(get_cards_for_players(get_stack(), players)[0][1]) == 6
assert len(get_cards_for_players(get_stack(), players)[1][1]) == 6
