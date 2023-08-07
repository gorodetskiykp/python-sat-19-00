number0 = ["****", "*  *", "*  *", "*  *", "****"]
number1 = ["  * ", " ** ", "* * ", "  * ", "****"]
number2 = [" ** ", "*  *", "   *", " *  ", "****"]
number3 = [" ***", "   *", " ***", "   *", " ***"]
number4 = ["   *", "  **", " * *", "****", "   *"]
number5 = ["****", "*   ", "*** ", "   *", "*** "]
number6 = ["****", "*   ", "****", "*  *", "****"]
number7 = ["****", "  * ", " *  ", " *  ", " *  "]
number8 = [" ** ", "*  *", " ** ", "*  *", " ** "]
number9 = ["****", "*  *", "****", "   *", "****"]


def check_num(number):
    if number == 0:
        return number0
    if number == 1:
        return number1
    elif number == 2:
        return number2
    elif number == 3:
        return number3
    elif number == 4:
        return number4
    elif number == 5:
        return number5
    elif number == 6:
        return number6
    elif number == 7:
        return number7
    elif number == 8:
        return number8
    elif number == 9:
        return number9

while True:
    printer = []
    try:
        current_number = list(map(int, input()))
        for process in range(5):
            for i in range(len(current_number)):
                one = check_num(current_number[i])
                printer.append(one[process])
            print(*printer)
            printer = []
        break
    except ValueError as error1:
        print("Обязательно нужно ввести число")
