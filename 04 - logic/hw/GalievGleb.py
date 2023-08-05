from random import randint

number1 = randint(2, 11)
number2 = randint(2, 11)
number3 = randint(2, 11)

print(f"Ты получил {number1} и {number2}")
choice = input("Нужна ли тебе карта?\nСкажи Yes или No: ")

if choice == "Yes":
    print(f"Ты получил еще карту {number3}")
    if number1 == 11:
        number1 = 1
    if number2 == 11:
        number2 = 1
    if number3 == 11:
        number3 = 1
    total_sum = sum([number1, number2, number3])
    print(f"Теперь у тебя {total_sum}")
    if total_sum < 21:
        print("Вы не проиграли")
    elif total_sum == 21:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
elif choice == "No":
    total_sum = sum([number1, number2])
    print(f"Твоя сумма карт: {total_sum}")
    if total_sum < 21:
        print("Вы не проиграли")
    elif total_sum == 21:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
else:
    print("Ты ввел неверные входные данные, попробуй снова!")
