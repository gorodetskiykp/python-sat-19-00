from cards import allocate_cards
from test_config import stack
stack_2 = ['A♥', '5♣', '6♠', 'K♠', '4♥', '7♦',  'Q♠', '10♠']

assert allocate_cards(stack) == {'♥': ['5♥', '8♥', 'A♥'], '♦': ['7♦'], '♣': [], '♠': ['6♠', '7♠', '10♠', 'Q♠']}
assert allocate_cards(stack_2) == {'♥': ['4♥', 'A♥'], '♦': ['7♦'], '♣': ['5♣'], '♠': ['6♠', '10♠', 'Q♠', 'K♠']}

