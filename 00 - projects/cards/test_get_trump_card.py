from cards import get_trump_card
from test_config import players, stack, suit_of_last_card_of_last_player, trump

assert len(get_trump_card(stack, players)) == 1
assert get_trump_card(stack, players) == trump
assert get_trump_card([], players) == suit_of_last_card_of_last_player
