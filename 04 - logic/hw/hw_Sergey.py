from random import randint


COUNTER_CARD = 2
card1 = randint(2, 11)
card2 = randint(2, 11)
list_cards = [card1, card2]
check_card = list_cards[0] + list_cards[1]
print("Ваши карты:", list_cards, "Счет:", check_card)


if check_card == 21:
    print("ВЫ ВЫЙГРАЛИ!")
elif check_card > 21:
    print("ВЫ ПРОИГРАЛИ!")
else:
    choice = input("Берем карту или нет? Ваш выбор:").upper()
    if choice == "ДА":
        COUNTER_CARD += 1
        new_card = randint(2, 11)
        list_cards.append(new_card)
        for nominal in range(len(list_cards) - 1):  # цикл для перебора карт и проверки номинала
            if list_cards[nominal] == 11:
                list_cards[nominal] = 1
                if check_card == 21:
                    print("ВЫ ВЫЙГРАЛИ!")
                    print("Ваши карты:", list_cards, "Счет:", check_card)
                elif check_card < 21:
                    print("ВЫ НЕ ПРОИГРАЛИ!")
                    print("Ваши карты:", list_cards, "Счет:", check_card)
                else:
                    print("ВЫ ПРОИГРАЛИ!")
                    print("Ваши карты:", list_cards, "Счет:", check_card)
                break
            else:
                check_card += new_card
                if check_card == 21:
                    print("ВЫ ВЫЙГРАЛИ!")
                    print("Ваши карты:", list_cards, "Счет:", check_card)
                elif check_card < 21:
                    print("ВЫ НЕ ПРОИГРАЛИ!")
                    print("Ваши карты:", list_cards, "Счет:", check_card)
                else:
                    print("ВЫ ПРОИГРАЛИ!")
                    print("Ваши карты:", list_cards, "Счет:", check_card)
                break
    else:
        print("ВЫ НЕ ПРОИГРАЛИ")
        print("Счет:", check_card)
