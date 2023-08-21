from cards import get_random_cards, get_stack

assert isinstance(get_random_cards(get_stack(), 4), list)
assert len(get_random_cards(get_stack(), 4)) == 4
