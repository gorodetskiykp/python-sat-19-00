from random import randint

# даем 2 карты игроку
card1 = randint(2, 11)
card2 = randint(2, 11)

# сообщаем ему о картах на руке
print('Вам выпали карты:', card1, card2)

# даём выбор, играть ли дальше
choice = input('Взять еще карту? : ')

# если согласился, то даём еще карту
# сразу меняем при третьей карты 11 на 1
if choice == 'да' or choice == 'Да' or choice == 'ДА' or choice == '+':
    card3 = randint(2, 11)
    if card1 == 11:
        card1 = 1
    elif card2 == 11:
        card2 = 1
    elif card3 == 11:
        card3 = 1
    final = card1 + card2 + card3  # сумма всех карт
    print('Сумма карт у вас в руке:', final)
else:
    final = card1 + card2
    print('Сумма карт у вас в руке:', final)

# выводим результат
if final == 21:
    print('Поздравляем! Вы выиграли °˖✧◝(⁰▿⁰)◜✧˖°')
elif final < 21:
    print('Почти! Но вы не проиграли (ง ื▿ ื)ว')
else:
    print('Увы! Вы проиграли (っ´ω`)ﾉ(╥ω╥)')
