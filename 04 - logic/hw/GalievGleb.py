from random import randint

def get_card():
    return randint(2, 11)

def play_game():
    number1 = get_card()
    number2 = get_card()

    print(f"Ты получил {number1} и {number2}")

    total_sum = number1 + number2

    while total_sum <= 21:
        choice = input("Нужна ли тебе карта?\nСкажи Yes или No: ")

        if choice == "Yes":
            new_card = get_card()
            print(f"Ты получил еще карту {new_card}")
            if new_card == 11 and total_sum + new_card > 21:
                new_card = 1
            total_sum += new_card
            print(f"Теперь у тебя {total_sum}")
        elif choice == "No":
            break
        else:
            print("Ты ввел неверные входные данные, попробуй снова!")

    if total_sum <= 21:
        print("Вы не проиграли")
    else:
        print("Вы проиграли")

play_game()

    