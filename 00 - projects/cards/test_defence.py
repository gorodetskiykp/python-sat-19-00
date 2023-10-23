from cards import defence

# Есть некозырная карта для боя
hand = ['5♥', '7♠', '8♥', '7♦', 'A♥', '6♠', 'Q♠', '10♠']
attack = {'6♥': None}
trump = '♠'
assert defence(hand, attack, trump) == {'6♥': '8♥'}
assert hand == ['5♥', '7♠', '7♦', 'A♥', '6♠', 'Q♠', '10♠']

# Нет некозырной карты для боя, но есть козырь
hand = ['7♠', '7♦', '6♠', 'Q♠', '10♠']
attack = {'6♥': None}
trump = '♠'
assert defence(hand, attack, trump) == {'6♥': '6♠'}
assert hand == ['7♠', '7♦', 'Q♠', '10♠']

# Нет некозырной карты для боя, и нет козыря
hand = ['7♦']
attack = {'6♥': None}
trump = '♠'
assert defence(hand, attack, trump) == None
assert hand == ['7♦', '6♥']

# Есть некозырные карты для боя
hand = ['5♥', '7♠', '8♥', '7♦', 'A♥', '6♠', 'Q♠', '10♠']
attack = {'6♥': None, '4♦': None}
trump = '♠'
assert defence(hand, attack, trump) == {'6♥': '8♥', '4♦': '7♦'}
assert hand == ['5♥', '7♠', 'A♥', '6♠', 'Q♠', '10♠']

# Нет некозырных карт для боя, но есть козыри
hand = ['5♥', '7♠', '3♦', '6♠', 'Q♠', '10♠']
attack = {'6♥': None, '4♦': None}
trump = '♠'
assert defence(hand, attack, trump) == {'6♥': '6♠', '4♦': '7♠'}
assert hand == ['5♥', '3♦', 'Q♠', '10♠']

# Для первой - есть некозырная карта для боя
# Для второй - нет некозырной карты для боя, но есть козырь
hand = ['7♥', '7♠', '3♦', '6♠', 'Q♠', '10♠']
attack = {'6♥': None, '4♦': None}
trump = '♠'
assert defence(hand, attack, trump) == {'6♥': '7♥', '4♦': '6♠'}
assert hand == ['7♠', '3♦', 'Q♠', '10♠']

# Для первой - есть некозырная карта для боя
# Для второй - нечем бить
hand = ['7♥', '3♦']
attack = {'6♥': None, '4♦': None}
trump = '♠'
assert defence(hand, attack, trump) == None
assert hand == ['7♥', '3♦', '6♥', '4♦']

# Для первой - нечем бить
# Для второй - нет некозырной карты для боя, но есть козырь
hand = ['5♥', '3♦', '9♠']
attack = {'10♠': None, '4♦': None}
trump = '♠'
assert defence(hand, attack, trump) == None
assert hand == ['5♥', '3♦', '9♠', '10♠', '4♦']
