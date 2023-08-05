number1 = "10"
number2 = 0

result = 0

try:
    result = number1 / number2
except ZeroDivisionError as e:
    print("number2 = 0 !!!")
    print(e)
except TypeError as e:
    print("Делить можно только числа!")
    print(e)
except Exception as e:
    print(e)

print(result)
