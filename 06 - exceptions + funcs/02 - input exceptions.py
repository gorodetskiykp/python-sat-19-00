while True:
    number1 = input("Number 1: ")
    number2 = input("Number 2: ")

    try:
        result = int(number1) / int(number2)
        break
    except ZeroDivisionError as e:
        print("number2 = 0 !!!")
        print(e)
    except ValueError as e:
        print("Делить можно только числа!")
        print(e)
    except Exception as e:
        print(e)

print(result)


# while True:
#     number1 = input("Number 1: ")
#     number2 = input("Number 2: ")
#
#     if number1.isdigit() and number2.isdigit():
#         pass
#     else:
#         print("Делить можно только числа!")
#         continue
#
#     if int(number2) == 0:
#         print("number2 = 0 !!!")
#         continue
#
#     result = int(number1) / int(number2)
#     break
#
# print(result)
