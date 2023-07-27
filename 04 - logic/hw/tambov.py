from random import randint


number = []
number.append(randint(2, 11))
number.append(randint(2, 11))
print(number)

if sum(number) == 21:
    print(sum(number), 'Вы выиграли!')
elif sum(number) == 22:
    print(sum(number), 'Вы проиграли!')
elif sum(number) < 21:
    choice = int(input("Сделайте свой выбор: "))
    if choice == 1:
        number_3 = randint(2, 11)
        print(number_3)
        number.append(number_3)
        if sum(number) == 21:
            print(sum(number), 'Вы выиграли!')
        elif 11 in number:
            number.remove(11)
            number.append(1)
            if sum(number) == 21:
                print(sum(number), 'Произошла замена 11, Вы выиграли!')
            else:
                print(sum(number), 'Произошла замена 11, Вы не проиграли')
        elif sum(number) < 21:
            print(sum(number), 'Вы не проиграли')
        else:
            print(sum(number), 'Вы проиграли')
    else:
        print(sum(number), 'Вы не проиграли')
