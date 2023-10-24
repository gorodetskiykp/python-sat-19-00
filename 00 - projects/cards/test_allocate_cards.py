from cards import allocate_cards
from test_config import stack
stack_2 = ['A♥', '5♣', '6♠', 'K♠', '4♥', '7♦',  'Q♠', '10♠']
assert allocate_cards(stack)
assert allocate_cards(stack_2)
