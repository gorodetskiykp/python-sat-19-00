from cards import sorted_cards
from test_config import stack, sorted_stack

assert sorted_cards(stack) == sorted_stack
assert sorted_cards([]) == []
