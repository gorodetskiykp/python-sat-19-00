"""Сплитование и объединение."""

text = 'Hello    world again'
print(text.split())  # ['Hello', 'world', 'again']

text = 'Hello,world again,Привет,Мир'
print(text.split(','))  # ['Hello', 'world again', 'Привет', 'Мир']


words = ['Hello', 'world', 'again']  # -> Hello world again
print('-'.join(words))
