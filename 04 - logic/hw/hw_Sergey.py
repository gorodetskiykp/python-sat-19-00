from random import randint

COUNTER_CARD = 2
card1 = randint(2, 11)
card2 = randint(2, 11)
list_cards = [card1, card2]
start_check = list_cards[0] + list_cards[1]
print("Ваши карты:", list_cards, "Счет:", start_check)

if start_check == 21:
    print("ВЫ ВЫЙГРАЛИ!")
elif start_check > 21:
    print("ВЫ ПРОИГРАЛИ!")
else:
    choice = input("Берем карту или нет? Ваш выбор:").upper()
    if choice == "ДА":
        for nominal in range(len(list_cards)):
            if list_cards[nominal] == 11:
                list_cards[nominal] = 1
                check_card = list_cards[0] + list_cards[1]
        COUNTER_CARD += 1
        new_card = randint(2, 11)
        if new_card == 11:
            new_card = 1
            list_cards.append(1)
            if check_card == 21:
                print("ВЫ ВЫЙГРАЛИ!")
                print("Ваши карты:", list_cards, "Счет:", check_card)
            elif check_card < 21:
                print("ВЫ НЕ ПРОИГРАЛИ!")
                print("Ваши карты:", list_cards, "Счет:", check_card)
            else:
                print("ВЫ ПРОИГРАЛИ!")
                print("Ваши карты:", list_cards, "Счет:", check_card)
        else:
            list_cards.append(new_card)
            check_card = list_cards[0] + list_cards[1] + new_card
            print("ВЫ НЕ ПРОИГРАЛИ!")
            print("Ваши карты:", list_cards, "Счет:", check_card)
    else:
        print("ВЫ НЕ ПРОИГРАЛИ!")
        print("Ваши карты:", list_cards, "Счет:", start_check)
