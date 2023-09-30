# list, list()
# numbers = list()
# numbers = []
# [1, 2, "hello", (1, 2)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[4])  # 5
print(numbers)
numbers[4] = "hello"
print(numbers)

numbers = numbers + numbers + [11, 12]
print(numbers)

vector = [None] * 10
print(vector)
vector[6] = 5.6
print(vector)

# print(dir(list))
"""
'append' - вставить элемент в конец списка
'clear' - очистка списка
'copy' - поверхностная копия
'count' - количество значений в списке
'extend' - расширить текущий список значениями другого списка
'index' - порядковый номер искомого элемента
'insert' - вставить элемент в указанную позицию списка
'pop' - извлечь элемент
'remove' - удаление по значению
'reverse' - развернуть список
'sort' - сортировка
"""
help(list.count)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.append(10)  # numbers + [10]
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.extend([10, 11, 12])  # numbers + [10, 11, 12]
numbers.append([10, 11, 12])  # numbers + [[10, 11, 12]]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, [10, 11, 12]]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.insert(1, 10)  # numbers[:1] + [10] + numbers[1:]
numbers.insert(1, 10)  # numbers[1:1] = [10]
                       # numbers[1:1] = [10, 12, 14]
                       # numbers[6] = [10, 12, 14]
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers.pop())  # 9
print(numbers)
print(numbers.pop(0))  # 1
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9]
numbers.remove(5)  # numbers[:4] + numbers[5:]
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9]
numbers.clear()  # numbers = []
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9]
numbers2 = numbers.copy()  # numbers2 = numbers[:]
print(numbers2)

numbers = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9]
numbers.reverse()  # numbers = [::-1]
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9, 1, 2]
numbers.sort()  # numbers = sorted(numbers)
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9, 1, 2]
print(sorted(numbers))
print(numbers)
