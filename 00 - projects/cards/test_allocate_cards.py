from cards import allocate_cards
from test_config import stack
stack_2 = ['5♣', 'K♠', '4♥', '7♦', 'A♥', '6♠', 'Q♠', '10♠']
assert allocate_cards(stack)
assert allocate_cards(stack_2)
