

def get_players(players_count: int):  # Принимает кол-во игроков
    name_players = []  # Список для имен игроков
    count = 0
    while count != players_count:  # цикл для добавления имен и проверки в черном списке
        name_gamer = input('Enter your name:')
        if name_gamer in black_list:  # Проверяем имя в черном списке.
            print('You\'re denied the game')
        else:
            name_players.append(name_gamer)
            count += 1
    return name_players  # Возвращает список имен


black_list = ['Oksana', 'Tanya', 'Max']

