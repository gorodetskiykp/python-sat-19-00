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


def star_draw():
    while True:
        printer = []
        try:
            current_number = list(map(int, input("Введите число:")))
        except ValueError:
            print("Обязательно нужно ввести число")
            continue
        for process in range(5):
            for digit in current_number:
                save_num = numbers[current_number[digit]]
                printer.append(save_num[process])
            print(*printer)
            printer = []
        break


star_draw()
