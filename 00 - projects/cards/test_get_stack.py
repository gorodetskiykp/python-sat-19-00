from cards import get_stack
from config import cards, marks

assert len(get_stack()) == 52
assert type(get_stack()) == list
assert isinstance(get_stack(), list)
assert '2♥' in get_stack()
assert 'A♠' in get_stack()
assert isinstance(get_stack()[0], str)
assert get_stack()[0][0] in cards
assert ord(get_stack()[0][1]) in [ord(mark) for mark in marks]
