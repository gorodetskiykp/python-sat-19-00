# Список - list - list() -> [1, 2, 3, 4, "text", 3.14, [1, 2, 3], (4, 5, 6)]
# - изменяемый

# Кортеж - tuple - tuple() -> (1, 2, 3, 4) - неизменяемый

numbers_tuple1 = (1, 2, 3, 4)
numbers_tuple2 = 1, 2, 3, 4
numbers_tuple3 = (1, )
numbers_tuple4 = 1,
numbers_tuple5 = ()
numbers_tuple6 = tuple()

print(1, 2, 3, 4)  # 4 аргумента int
print((1, 2, 3, 4))  # 1 аргумент tuple

# print(type(numbers_tuple1))
# print(type(numbers_tuple2))
# print(type(numbers_tuple3))
# print(type(numbers_tuple4))
# print(type(numbers_tuple5))
# print(type(numbers_tuple6))

numbers_list1 = [1, 2, 3, 4]
numbers_list3 = [1]
numbers_list5 = []
numbers_list6 = list()

# print(type(numbers_list1))
# print(type(numbers_list3))
# print(type(numbers_list5))
# print(type(numbers_list6))

numbers_tuple1 = (1, 2, 3, 4)  # счёт начинается с 0 слева и с -1 справа
print(numbers_tuple1[0])  # 1
print(numbers_tuple1[1])  # 2
print(numbers_tuple1[3])  # 2
print(numbers_tuple1[-1])  # 4

numbers_list1 = [1, 2, 3, 4, 5]
print(numbers_list1[-1])  # 5

str_is_collection_too = "hello"
print(str_is_collection_too[0])  # h
print(str_is_collection_too[-1])  # o

numbers_list1 = [1, 2, 3, 4, 5]
print(numbers_list1)
print(id(numbers_list1[0]))
print(numbers_list1[0])  # 1
numbers_list1[0] = "A"
print(numbers_list1)
print(id(numbers_list1[0]))

numbers_tuple1 = (1, 2, 3, 4)
# numbers_tuple1[0] = "A"  # TypeError: 'tuple' object does not support item assignment

# !!! ***
magic_tuple = (1, 2, "text", (3, 4), [5, 6])
print()
print(magic_tuple)
print(magic_tuple[4])
magic_tuple[4][0] = "MAGIC!!"
print(magic_tuple)

# len - количество элементов, длина коллекции, размер коллекции (int)
print('Длина кортежа:', len(magic_tuple))
