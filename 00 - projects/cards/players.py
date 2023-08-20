from config import black_list


def get_players(players_count: int) -> list:
    players = []
    while len(players) < players_count:
        name = input('Введите имя игрока: ').strip()
        if name in black_list:
            print('Игрок в чёрном списке')
        elif name in players:
            print('Игрок уже добавлен')
        else:
            players.append([name, []])
    return players
