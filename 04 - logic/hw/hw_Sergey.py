from random import randint


counter_card = 2
check_card = randint(2, 11) + randint(2, 11)
print("Счет:", check_card)


if check_card == 21:
    print("ВЫ ВЫЙГРАЛИ!")
    print("Счет:", check_card)
else:
    while check_card < 21:
        choice = input("Берем карту или нет? Ваш выбор:").upper()
        if choice == "ДА":
            counter_card += 1
            new_card = randint(2, 11)
            if new_card == 11:
                new_card = 1
                check_card += new_card
                print("Счет:", check_card)
                if check_card == 21:
                    print("ВЫ ВЫЙГРАЛИ!")
                    print("Счет:", check_card)
                    break
            else:
                check_card += new_card
                print("Счет:", check_card)
        else:
            print("ВЫ НЕ ПРОИГРАЛИ")
            print("Счет:", check_card)
            break
    if check_card > 21:
        print("ВЫ ПРОИГРАЛИ")
