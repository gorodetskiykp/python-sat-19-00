from cards import get_cards_for_players, get_random_cards, get_stack
from config import cards, marks
from game import view_cards

assert len(marks) == 4

view_cards(players)
view_cards(get_cards_for_players(get_stack(), players))
