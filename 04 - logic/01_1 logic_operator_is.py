number5 = 5
number_five = 2 + 3
print(id(number5))
print(id(number_five))

# Проверка идентичности - равенство адресов
print(number5 is number_five)

list1 = [1, 2, 3]
list2 = list1

print(id(list1))
print(id(list2))

print(list1 is list2)

list2[0] = "CHANGED!!"
print(list1)
print(list2)

list3 = list1.copy()  # copy list
print(id(list3))
print(list1 is list3)
print(list1 == list3)
