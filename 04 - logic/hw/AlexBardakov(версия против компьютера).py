from random import randint

hand = []  # Запоминаем карты с руки, чтобы выводить потом ч/з print
card1 = randint(2, 11)
card2 = randint(2, 11)

comp_hand = []  # У компьютера теперь тоже есть ручки
comp_card1 = randint(2, 11)
comp_card2 = randint(2, 11)


def yes():
    new_card = randint(2, 11)
    hand.append(new_card)
    print("У вас на руках карты:", hand,
          "Ваша сумма карт:", sum(hand), "Нужна ли еще карта? да/нет")
    global choice
    choice = input("Сделайте свой выбор:")


def lose():
    print("ВЫ ПРОИГРАЛИ!")
    return


hand.append(card1)  # Берем в руку первые карты
hand.append(card2)
comp_hand.append(comp_card1)  # Компьютеру тоже даем карты, все честно
comp_hand.append(comp_card2)

# Сначала посмотрим, что у компьютера и разберемся со своей рукой
print("У вас на руках карты:", hand, "Ваша сумма карт:", sum(hand),
      "\nУ компьютера:", comp_hand, "\nНужна ли еще карта? да/нет")
choice = input("Сделайте свой выбор:")

while choice == "да":
    yes()

if choice == "нет":
    print("У вас на руках карты:", hand,
          "\nВаша сумма карт:", sum(hand))

# Условие моментального проигрыша
if sum(hand) > 21:
    lose()

# Компьютер производит добор карт. Да, он жульничает.
while sum(comp_hand) < 17 and sum(hand) > sum(comp_hand):
    new_card = randint(2, 11)
    comp_hand.append(new_card)
    print("У компьютера:", comp_hand, "\nВсего:", sum(comp_hand))

print("Считаем результат! Сумма ваших карт:", sum(hand),
      "\nУ компьютера:", sum(comp_hand))

if sum(hand) <= 21 and (sum(comp_hand) > 21 or sum(comp_hand) < sum(hand)) :
    print("ВЫ ВЫИГРАЛИ")
elif sum(comp_hand) == sum(hand):
    print("НИЧЬЯ")
else:
    print("ВЫ ПРОИГРАЛИ")
