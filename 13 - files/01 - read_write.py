# int, bool, float, str
# list, tuple, set, dict

# if-elif-else
# for-in, while
# try-except

# in-out

# ЧТЕНИЕ

# file = open('text.txt', 'r', encoding='utf8')
file = open('text.txt', encoding='utf8')
# file = open('../04 - logic/text.txt')
# file = open('C:\\temp\\text.txt')
# file = open('/tmp/text.txt')
print(file)
print()
text = file.read()  # чтение всего содержимого файла
file.seek(0)  # передвинуть курсор на 0 позицию
file.seek(2)  # передвинуть курсор на 2 позицию

print(text)
print(file.read())

file.close()

# text = file.read()  # ValueError: I/O operation on closed file.


file = open('text.txt', encoding='utf8')
line1 = file.readline()  # считать одну строку
line2 = file.readline()  # считать следующую строку
line3 = file.readline()  # не хватило строки
file.close()

print(line1)
print(line2)
print(line3)

file = open('text.txt', encoding='utf8')
lines = file.readlines()  # считать все строки в список
file.close()

print(lines)


# НОВЫЙ СИНТАКСИС
with open('text.txt', encoding='utf8') as file:
    line1 = file.readline()

print(line1)


# ЗАПИСЬ

data = 'Привет Мир!!\n'
with open('output.txt', 'w', encoding='utf8') as file:
    file.write(data)
    file.write("Hello world!")
    # print(file.read())  # io.UnsupportedOperation: not readable

# ДОБАВЛЕНИЕ
with open('output.txt', 'a', encoding='utf8') as file:
    file.write("\n??")


with open('print.txt', 'w') as f:
    for item in range(10):
        print(item, item ** 2, sep=': ', end=', ', file=f)
