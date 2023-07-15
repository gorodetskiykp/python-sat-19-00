# списки

numbers_tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
numbers_list = list(numbers_tuple)

print(numbers_list)
print(type(numbers_list))

# Класс (Тип, Шаблон) -> Объект (Экзмпляр)
# - свойства (описание)
# - методы (действия) - dir(object_name) / dir(type_name)
#   - магические  __method_name__()
#   - служебные  _method_name()
#   - обычные method_name()

# print(dir(numbers_list))

# function_name(object_name, args)
# object_name.method_name(args)

print()
print(numbers_list)
numbers_list.append(11)  # append - добавить элемент в конец списка
print(numbers_list)
numbers_list.remove(2)  # remove - удалить первый элемент == 2
print(numbers_list)
numbers_list.append(3)
numbers_list.append(3)
numbers_list.append(3)
numbers_list.append(3)
numbers_list.append(3)
print(numbers_list)
numbers_list.remove(3)
print(numbers_list)
numbers_list.insert(1, 2)  # добавить на 1-ую позицию число 2
print(numbers_list)

# print(dir(tuple)) - 'count', 'index'
# print(dir(str))

# print(help(list.insert)) - вызов справки по методу

print(help(list))
