"""
    Принимает количество игроков,
    спрашивает у пользователя имя каждого игрока.
    Проверяем имя в черном списке.
    Возвращает список имен
    """


def get_players(players_count: int):
    name_players = []
    for _ in range(players_count):
        name_gamer = input('Enter your name:')
        if name_gamer in black_list:
            print('You\'re denied the game')
        else:
            name_players.append(name_gamer)
    return list(name_players)


black_list = []
print(get_players(players_count=5))
