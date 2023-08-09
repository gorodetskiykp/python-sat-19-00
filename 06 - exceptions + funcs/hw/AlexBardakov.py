numbers = [["****", "*  *", "*  *", "*  *", "****"],
           ["  * ", " ** ", "* * ", "  * ", "****"],
           [" ** ", "*  *", "   *", " *  ", "****"],
           [" ***", "   *", " ***", "   *", " ***"],
           ["   *", "  **", " * *", "****", "   *"],
           ["****", "*   ", "*** ", "   *", "*** "],
           ["****", "*   ", "****", "*  *", "****"],
           ["****", "  * ", " *  ", " *  ", " *  "],
           [" ** ", "*  *", " ** ", "*  *", " ** "],
           ["****", "*  *", "****", "   *", "****"]]


def star_line():  # создаем единый список символов в строку
    intermediate = []
    for process in range(5):
        for digit in range(len(current_number)):
            save_num = numbers[current_number[digit]]
            intermediate.append(save_num[process])
    return intermediate


def star_list():  # делим список по длине введеного числа
    draw_list = (star_line()[i:i + 5] for i in range(0, len(star_line()), 5))
    return list(draw_list)


current_number = []
while True:
    try:
        current_number = list(map(int, input("Введите число:")))
    except ValueError:
        print("Обязательно нужно ввести число")
        continue
    break
for string in range(5):
    print(*star_list()[string])

