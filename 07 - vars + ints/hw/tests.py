from cards import get_cards_for_players, get_random_cards, get_stack
from config import cards, marks
from game import view_cards

assert len(marks) == 4

assert len(get_stack()) == 52
assert type(get_stack()) == list
assert isinstance(get_stack(), list)
assert '2♥' in get_stack()
assert 'A♠' in get_stack()
assert isinstance(get_stack()[0], str)
assert get_stack()[0][0] in cards
# assert get_stack()[0][1] in marks
assert len(get_random_cards(get_stack(), 4)) == 4
assert isinstance(get_random_cards(get_stack(), 4), list)

players = [['p1', ['2♥']], ['p2', []]]
assert isinstance(get_cards_for_players(get_stack(), players), list)
assert len(get_cards_for_players(get_stack(), players)[0][1]) == 6
assert len(get_cards_for_players(get_stack(), players)[1][1]) == 6

view_cards(players)
view_cards(get_cards_for_players(get_stack(), players))
