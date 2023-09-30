# text = "123"
# print(id(text))
# text2 = text
# print(id(text2))
# text = "234"
# print(id(text))
# print(id(text2))
# print(text)
# print(text2)

numbers = [1, 2, 3]  # addr = ff1
numbers[0]  # ff1 -> ab4
numbers2 = numbers  # addr = ff1

numbers[0] = 10  # ff1 -> del(ab4) -> ac6

print(numbers)
print(numbers2)


def change_1st_item(lst):
    lst[0] = "HELLO"


stack = ["2", "3", "A"]
print(stack)
arg = stack
change_1st_item(arg)
print(stack)

print("-" * 30)
numbers = [1, 2, 3]
numbers2 = numbers.copy()
numbers2[-1] = "THE END"
print(numbers)
print(numbers2)

numbers = numbers[:]  # копия

print("-" * 30)
numbers = [1, 2, 3, ["a", "b"]]
numbers2 = numbers.copy()
numbers2[-1][-1] = "THE END"
print(numbers)
print(numbers2)
