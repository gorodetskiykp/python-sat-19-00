from cards import get_minimal_card, sorted_cards
from test_config import (
    minimal_card_in_all_stack,
    stack,
    trump
)

assert get_minimal_card(stack) == minimal_card_in_all_stack
assert get_minimal_card([]) == None
assert get_minimal_card(stack, trump) == minimal_card_in_all_stack
