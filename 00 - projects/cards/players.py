from config import black_list
from random import randint

def get_players(players_count: int) -> list:
    players = []
    players_names = []
    while len(players) < players_count:
        name = input('Введите имя игрока: ').strip()
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
            [['p1', ['k1', 'k2', ...]], ['p2', ['k1', 'k2', ...]]]
        tramp_mark - строчное значение козырной масти
    Возвращаемое значение:
        Порядковый номер игрока, который начинает игру
    """
    tramp_cards = []
    random_start = randint(1, 4)
    for index in players:
        for card in players[index][1]:
            if tramp_mark in card:
                tramp_cards.append(players[index][1])
        index += 1
    if len(tramp_cards) > 0:
        sorted(tramp_cards)
        for digit in players:
            if tramp_cards[1] in players[digit]:
                start_player_num = digit+1
            else:
                digit += 1
    else:
        start_player_num = random_start
    return start_player_num


def move(hand: list, card: list):
    """Убрать карту из карт игрока.

    Аргументы:
        hand - список карт у игрока
        card - строчное значение карты, которую нужно выложить на стол
    Возвращаемое значение:
        Строчное значение карты
    """
