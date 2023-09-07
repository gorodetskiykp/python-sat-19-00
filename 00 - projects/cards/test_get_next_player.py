from players import get_next_player

assert get_next_player(0, 2) == 1
assert get_next_player(1, 3) == 2
assert get_next_player(1, 2) == 0
