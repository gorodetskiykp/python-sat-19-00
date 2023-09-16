from cards import get_minimal_card, sorted_cards
from config import cards, marks
from test_config import (
    minimal_card_in_all_stack,
    stack,
    trump
)

assert get_minimal_card(stack) == minimal_card_in_all_stack
assert get_minimal_card([]) == None
assert get_minimal_card(stack, trump) == minimal_card_in_all_stack
assert isinstance(get_minimal_card(stack, trump), str)
assert len(get_minimal_card(stack, trump)) in (2, 3)
assert get_minimal_card(stack, trump)[:-1] in cards
assert get_minimal_card(['10♥', '7♠', '10♦'], '♠')[:-1] in cards
assert get_minimal_card(stack, trump)[-1] in marks
assert get_minimal_card(['5♥', '7♥', '8♥', '10♥'], '♥') == '5♥'
