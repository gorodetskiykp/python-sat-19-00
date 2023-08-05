from random import randint

# даем 2 карты игроку
card_list = [randint(2, 11), randint(2, 11)]

# сообщаем ему о картах на руке
print('Вам выпали карты:', card_list)

# даём выбор, играть ли дальше
# если согласился, то даём еще карту
while True:
    choice = input('Взять еще карту? (да/нет): ').strip().lower()  # переменная д\н
    if choice == 'да':
        card_list.append(randint(2, 11))
        if 11 in card_list:  # проверка на 11
            card_list.remove(11)
            card_list.append(1)
        print('Вам выпали карты:', card_list,
              'Сумма ваших карт:', sum(card_list))
    if sum(card_list) == 21:
        print('Поздравляем! Вы выиграли °˖✧◝(⁰▿⁰)◜✧˖°')
        break
    if sum(card_list) > 21:
        print('Увы! Вы проиграли (っ´ω`)ﾉ(╥ω╥)')
        break
    if choice == 'нет':
        if sum(card_list) == 21:
            print('Поздравляем! Вы выиграли °˖✧◝(⁰▿⁰)◜✧˖°')
            break
        if sum(card_list) > 21:
            print('Увы! Вы проиграли (っ´ω`)ﾉ(╥ω╥)')
            break
        if sum(card_list) < 21:
            print('Почти! Но вы не проиграли (ง ื▿ ื)ว')
            break
