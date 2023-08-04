import sys
from random import randint


def rand():  # Исправил повторы, загнал под функцию
    a = randint(2, 11)
    if a == 11 and ((sum(hand)+11) > 21 or (sum(comp_hand)+11) > 21):
        a = 1  # Дополнил возможность замены для ПК при доборе
    return a


hand = [rand(), rand()]  # Максимально упростил набор, убрал лишние ф-ции
comp_hand = [rand(), rand()]

print("У вас на руках карты:", hand, "Ваша сумма карт:", sum(hand),
      "\nУ компьютера:", comp_hand[0], "\nНужна ли еще карта? да/нет")

for i in range(10):  # Оставил цикл for, чтобы был. Можно просто заменить на while.
    choice = input("Сделайте свой выбор:").strip().lower()
    if choice == "да":  # Воспользовался приемом из занятия для упрощения
        new_card = randint(2, 11)
        hand.append(new_card)
        if sum(hand) > 21:
            if 11 in hand:
                hand.remove(11)
                hand.append(1)
                print("У вас на руках карты:", hand,
                      "Ваша сумма карт:", sum(hand), "Нужна ли еще карта? да/нет")
            else:
                print("Ваша сумма карт:", sum(hand), "\nВЫ ПРОИГРАЛИ!")
                sys.exit()
        else:
            print("У вас на руках карты:", hand,
                  "Ваша сумма карт:", sum(hand), "Нужна ли еще карта? да/нет")
    elif choice == "нет":
        print("У вас на руках карты:", hand, "Ваша сумма карт:", sum(hand))
        break

# Компьютер производит добор карт.
while True:
    if sum(comp_hand) > 21:
        if 11 in comp_hand:  # Теперь компьютер тоже получает замену
            comp_hand.remove(11)
            comp_hand.append(1)
    if sum(comp_hand) > 17 or sum(comp_hand) > sum(hand):
        break  # Процесс тормозит только если ПК набрал 18 или больше игрока
    new_card = rand()  # Сначала проверяем условия, потом производим добор
    comp_hand.append(new_card)

print("У компьютера:", comp_hand, "Всего:", sum(comp_hand))

if sum(hand) <= 21 and (sum(comp_hand) > 21 or sum(comp_hand) < sum(hand)):
    print("ВЫ ВЫИГРАЛИ")
elif sum(comp_hand) == sum(hand):
    print("НИЧЬЯ")
else:
    print("ВЫ ПРОИГРАЛИ")
