from cards import get_trump_card
from test_config import stack, trump

assert len(get_trump_card(stack)) == 1
assert get_trump_card(stack) == trump
assert get_trump_card([]) is None
