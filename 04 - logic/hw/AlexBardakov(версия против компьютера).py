import sys
from random import randint


def rand():  # Исправил повторы, загнал под функцию
    a = randint(2, 11)
    if a == 11 and sum(hand):
        a = 1
    return a


def yes():
    new_card = randint(2, 11)
    hand.append(new_card)


hand = []  # Запоминаем карты с руки, чтобы выводить потом ч/з print
card1 = rand()
card2 = rand()

comp_hand = []  # У компьютера теперь тоже есть ручки
comp_card1 = rand()
comp_card2 = rand()

hand.append(card1)  # Берем в руку первые карты
hand.append(card2)
comp_hand.append(comp_card1)  # Компьютеру тоже даем карты, все честно
comp_hand.append(comp_card2)

# Мы видим свою руку и одну карту крупье
print("У вас на руках карты:", hand, "Ваша сумма карт:", sum(hand),
      "\nУ компьютера:", comp_hand[0], "\nНужна ли еще карта? да/нет")

for i in range(10):  # Использовал цикл for, чтобы убрать global
    choice = input("Сделайте свой выбор:")
    if choice in ["да", "Да", "ДА"]:
        yes()
        if sum(hand) > 21:
            if 11 in hand:  # Условие замены 11 на 1
                hand.remove(11)
                hand.append(1)
                print("У вас на руках карты:", hand,
                      "Ваша сумма карт:", sum(hand), "Нужна ли еще карта? да/нет")
            else:  # Условие моментального проигрыша
                print("Ваша сумма карт:", sum(hand),"\nВЫ ПРОИГРАЛИ!")
                sys.exit()
        else:
            print("У вас на руках карты:", hand,
                  "Ваша сумма карт:", sum(hand), "Нужна ли еще карта? да/нет")
    elif choice in ["нет", "Нет", "НЕТ"]:
        print("У вас на руках карты:", hand, "Ваша сумма карт:", sum(hand))
        break

# Компьютер производит добор карт. Да, он жульничает.
while sum(comp_hand) < 17 and sum(hand) > sum(comp_hand):
    new_card = rand()
    comp_hand.append(new_card)

# Компьютер вскрывается
print("У компьютера:", comp_hand, "Всего:", sum(comp_hand))

if sum(hand) <= 21 and (sum(comp_hand) > 21 or sum(comp_hand) < sum(hand)) :
    print("ВЫ ВЫИГРАЛИ")
elif sum(comp_hand) == sum(hand):
    print("НИЧЬЯ")
else:
    print("ВЫ ПРОИГРАЛИ")
