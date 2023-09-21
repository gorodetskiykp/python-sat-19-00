from cards import get_minimal_similar_cards

tramp = '♠'

stack = []

hand = ['5♥', '7♠', '8♥', '7♦', 'A♥', '6♠', 'Q♠', 'A♠', 'A♣', '10♣']
assert get_minimal_similar_cards(hand, tramp, stack) == [['7♠', '7♦'], ['A♥', 'A♠', 'A♣']]

hand = ['5♥', '7♠', '8♥', '7♦', 'A♥', '6♠', 'Q♠', 'A♠', 'A♣', '10♣', '9♠', '9♦']
assert get_minimal_similar_cards(hand, tramp, stack) == [['7♠', '7♦'], ['A♥', 'A♠', 'A♣']]

hand = ['9♥', '7♠', '8♥', '7♦', 'A♥', '6♠', 'Q♠', 'A♠', 'A♣', '10♣', '9♠', '9♦']
assert get_minimal_similar_cards(hand, tramp, stack) == [['7♠', '7♦'], ['9♥', '9♠', '9♦']]

hand = []
assert get_minimal_similar_cards(hand, tramp, stack) == []

hand = ['5♥', '8♥', '7♦', 'A♥', '6♠', 'Q♠', 'A♠', 'A♣', '10♣']
assert get_minimal_similar_cards(hand, tramp, stack) == [['A♥', 'A♠', 'A♣']]

hand = ['5♥', '8♥', '7♦', '6♠', 'Q♠', 'A♠', '10♣']
assert get_minimal_similar_cards(hand, tramp, stack) == []

stack = ['2♥']

hand = ['5♥', '7♠', '8♥', '7♦', 'A♥', '6♠', 'Q♠', 'A♠', 'A♣', '10♣']
assert get_minimal_similar_cards(hand, tramp, stack) == [['A♥', 'A♣']]

hand = []
assert get_minimal_similar_cards(hand, tramp, stack) == []

hand = ['5♥', '8♥', '7♦', 'A♥', '6♠', 'Q♠', 'A♠', 'A♣', '10♣']
assert get_minimal_similar_cards(hand, tramp, stack) == [['A♥', 'A♣']]

hand = ['5♥', '8♥', '7♦', '6♠', 'Q♠', 'A♠', '10♣']
assert get_minimal_similar_cards(hand, tramp, stack) == []
