from random import randint

TARGET = 21
TO_CHANGE = 11
numbers = []
numbers.append(randint(2, 11))
numbers.append(randint(2, 11))
print(numbers)

goal = 0
for number in numbers:
    goal += number
print(goal)
choice = input("Сделайте свой выбор, y/n: ")
if choice == 'y':
    number_3 = randint(2, 11)
    print(number_3)
    numbers.append(number_3)
    for number in numbers:
        if number == TO_CHANGE:
            numbers.remove(11)
            numbers.append(1)
print(numbers)
if sum(numbers) == TARGET:
    print(sum(numbers), 'Вы выиграли!')
if sum(numbers) < TARGET:
    print(sum(numbers), 'Вы не проиграли')
if sum(numbers) > TARGET:
    print(sum(numbers), 'Вы проиграли')
