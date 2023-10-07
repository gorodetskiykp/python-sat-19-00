from config import min_count_of_players, max_count_of_players, names
from players import random_players
from random import randint

players_count = randint(min_count_of_players, max_count_of_players)

assert len(random_players(players_count)) in (2, 3, 4)

for name in random_players(players_count):
    assert name in names

assert isinstance(random_players(players_count), list)