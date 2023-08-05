# 3 аргумента
# типы: int / str
# сложить как int


def to_num(value):
    if type(value) == str:
        if value.isdigit():
            value = int(value)
        else:
            value = 0
    return value


def to_num(value):
    if type(value) == str:
        if value.isdigit():
            return int(value)
        return 0


def to_num(value):
    try:
        return float(value)
    except:
        return 0


num1 = "1"
num2 = 2
num3 = 10 / 4

num1 = to_num(num1)
num2 = to_num(num2)
num3 = to_num(num3)


result = num1 + num2 + num3
print(result)
