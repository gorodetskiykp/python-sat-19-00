from random import randint

from config import black_list, cards
from cards import get_minimal_card


def get_players(players_count: int) -> list:
    players = []
    players_names = []
    while len(players) < players_count:
        name = input('Введите имя игрока: ').strip()
        if len(name) < 3:
            print('Имя должно содержать минимум 3 символа. Попробуйте ещё раз')
        elif name in black_list:
            print('Игрок в чёрном списке')
        elif name in players_names:
            print('Такой игрок уже есть')
        else:
            players.append([name, []])
            players_names.append(name)
    return players


def first_move(players: list, trump_mark: str) -> int:
    """Определить игрока, который начнёт игру.
    Нужно проверить карты игроков и найти минимальный козырь
    Если ни у кого нет козырей, ходит игрок № 0

    Аргументы:
        players - список игроков и из карт
            [
                ['p1', ['k1', 'k2', ...]],
                ['p2', ['k1', 'k2', ...]],
            ]
        trump_mark - строчное значение козырной масти
    Возвращаемое значение:
        Порядковый номер игрока, который начинает игру
    """
    tramp_cards = []
    for _, cards in players:
        for card in cards:
            if trump_mark in card:
                tramp_cards.append(card)
    player_no = 0
    if tramp_cards:
        min_tramp_card = get_minimal_card(tramp_cards)
        for _, cards in players:
            if min_tramp_card in cards:
                return player_no
            player_no += 1
    return 0


def move(hand: list, card: str):
    """Убрать карту из карт игрока.

    Аргументы:
        hand - список карт у игрока
        card - строчное значение карты, которую нужно выложить на стол
    Возвращаемое значение:
        Строчное значение карты
    """
    hand.remove(card)
    return hand


def movement(hand: list):
    """Убрать карту из карт игрока.

    Аргументы:
        hand - список карт у игрока
        card - строчное значение карты, которую нужно выложить на стол
    Возвращаемое значение:
        Строчное значение карты
    """
    table = []
    row = []
    print('У вас на руке:', *hand)
    card_num = int(input('Какой картой вы хотите сходить?(1,2,..,6,..)')) - 1
    card = hand[card_num]
    hand = move(hand, card)
    table.append(list(card))
    for cards in hand:
        if card[:-1] in cards:
            row.append(cards)
    print('Вы так же можете выложить', *row)
    if input('Будем выкладывать?(да/нет)').strip().lower() == 'да':
        for cards in row:
            table.append(list(cards))
            hand = move(hand, cards)
    return table


def defence(hand: list, table: list, trump_mark: str):
    take_to_hands = False  # если не отбили - меняем на True
    for tab_cards in table:
        skip = ''  # для игнорирования карты, которой только что отбились
        for card in tab_cards:
            if skip == card:
                continue
            stop_index = 1  # параметр сработает только если не сможем отбиться
            bit_bat = []  # список карт, которыми сможем отбить карту со стола
            for cardstr in hand:
                card_value = card[:-1]  # убираем масть у карты для сравнения
                cardstr_value = cardstr[:-1]
                # добавляем сравнение карт по старшенству.
                if (card[-1] in cardstr and
                        cards.index(cardstr_value) > cards.index(card_value)):
                    bit_bat.append(cardstr)
                # избегаем сравнения козырей между собой, они отпадут в if
                elif trump_mark in cardstr and trump_mark != cardstr[-1]:
                    bit_bat.append(cardstr)
            print('Ваша рука:', *hand)
            print('Карты на столе:', *table)
            if bit_bat:
                print('Вы можете отбить', card, 'c помощью',
                      ', '.join(map(str, bit_bat)),
                      'Чем будем отбивать?(1,2,3,...)')
                while True:
                    try:
                        num = int(input('Введите номер карты'))
                        break
                    except:
                        print('Введите существующий порядковый номер карты')
                        continue
                bit = bit_bat[num - 1]
                print('Отбиваем', bit)
                hand.remove(bit)
                tab_cards.append(bit)
                skip = bit  # игнорируем карту, которой отбились в сл.итерации
                stop_index = 0
            else:
                print('Отбить не получится, забираем карты на руку')
            if stop_index == 1:
                take_to_hands = True
                break
    print('Карты на столе:', *table)
    if take_to_hands:
        for tab_cards in table:
            for card in tab_cards:
                hand.append(card)
    return hand