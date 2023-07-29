nums = [1, 2, 3]
length = len(nums)
idx = 0

while idx < length:
    print(nums[idx], nums[idx] ** 2)
    idx += 1

print()
number = 0
while True:
    number += 1
    if number % 2 == 0:
        continue
    if number ** 2 > 250:
        break
    print(number, number ** 2)
else:
    print("Нам не встретились большие числа!")



