from random import randint

hand = []  # Запоминаем карты с руки, чтобы выводить потом ч/з print
card1 = randint(2, 11)
card2 = randint(2, 11)

def yes():
    new_card = randint(2, 11)
    hand.append(new_card)
    print("У вас на руках карты:", hand,
          "Ваша сумма карт:", sum(hand), "Нужна ли еще карта? да/нет")
    global choice
    choice = input("Сделайте свой выбор:")


hand.append(card1)  # Берем в руку первые карты
hand.append(card2)

print("У вас на руках карты:", hand,
      "Ваша сумма карт:", sum(hand), "Нужна ли еще карта? да/нет")
choice = input("Сделайте свой выбор:")

while choice == "да":
    yes()

if choice == "нет":
    print("У вас на руках карты:", hand,
          "Ваша сумма карт:", sum(hand), "Считаем результаты!")

if sum(hand) < 21:
    print("ВЫ НЕ ПРОИГРАЛИ")
elif sum(hand) == 21:
    print("ВЫ ВЫИГРАЛИ")
else:
    print("ВЫ ПРОИГРАЛИ")
