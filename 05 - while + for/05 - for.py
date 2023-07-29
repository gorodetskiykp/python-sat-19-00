nums = [1, 2, 3, 4, 3, 2, 0, 1, 2, 3]


for number in nums:
    if number == 0:
        break
    if number % 2 == 0:
        continue
    print(number, number ** 2)
else:
    print("Нулей не было")


