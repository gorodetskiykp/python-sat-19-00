from config import black_list


def get_players(players_count: int) -> list:
    players = []
    players_names = []
    while len(players) < players_count:
        name = input('Введите имя игрока: ').strip()
        if len(name) < 3:
            print('Имя должно содержать минимум 3 символа. Попробуйте ещё раз')
            continue
        if name in black_list:
            print('Игрок в чёрном списке')
        elif name in players_names:
            print('Игрок уже добавлен')
        else:
            players.append([name, []])
            players_names.append(name)
    return players


def first_move(players: list, tramp_mark: str) -> int:
    """Определить игрока, который начнёт игру.
    Нужно проверить карты игроков и найти минимальный козырь

    Аргументы:
        players - список игроков и из карт
            ['p1', ['k1', 'k2', ...], 'p2', ['k1', 'k2', ...]]
        tramp_mark - строчное значение козырной масти
    Возвращаемое значение:
        Порядковый номер игрока, который начинает игру
    """


def move(hand: list, card: list):
    """Убрать карту из карт игрока.

    Аргументы:
        hand - список карт у игрока
        card - строчное значение карты, которую нужно выложить на стол
    Возвращаемое значение:
        Строчное значение карты
    """
