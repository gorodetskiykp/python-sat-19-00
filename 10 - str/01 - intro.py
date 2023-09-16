"""Строки."""

# str - str() - неизменяемый тип

word = 'Hello'
print(word)
print(id(word))

word = 'Hello' + '!'
print(word)
print(id(word))

words = "Hello i'm" + 'World i\'m' + '''Привет''' + """Мир"""


def some_func():
    """Это какая-то функция."""


words = "Hello" + \
        "World"

words = ("Hello"
         "World")

text = """Это
многострочный
текст"""

# Спецсимволы

# символ новой строки \n
print('Первая строка\nВторая строка')

# отступ/TAB \t
print('\tПервая строка\n\tВторая строка')

# слэш \\
print('Первая строка\nВторая строка\\инструкция')

# дополнительные литералы
print('Стоимость: 80\N{euro sign}')
print('Стоимость: 80\u20AC')
print('Стоимость: 80\U000020AC')
print('Стоимость: 80', chr(0x20AC))

# Строки - коллекции
word = 'Hello'
print(len(word))  # 5
print('H' in word)  # True
print('Hell' in word)  # True
print('h' in word)  # False
print(word[0])  # H
print(word[4])  # o
print(word[-1])  # o
print(word[-5])  # H

# word[0] = 'h' -> ERROR
