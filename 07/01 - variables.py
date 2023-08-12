its_my_apples = 5  ## !!! ASCII
# 3var = 5  # Error
# _special_count = 10  # служебные переменные
# __super_special = 15  # приватные переменные
# __gt__() = 10  # магические методы

# str, int, - не используйте зарезервированные слова для имен переменных

print(dir(__builtins__))
print()
# _

for _ in range(5):
    print("Hello")
print()


def operations(num1, num2):
    summ = num1 + num2
    division = num1 - num2
    return summ, division


results = operations(1, 2)
sum_res, div_res = operations(1, 2)
sum_res1, _ = operations(1, 2)
print(results)
print(sum_res)
print(div_res)
print(sum_res1)

