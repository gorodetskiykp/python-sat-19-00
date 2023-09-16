"""Форматирование."""

name = 'Артём'
age = 39

# Привет! Я - Артём, мне 39 лет

print('Привет! Я - ' + name + ', мне ' + str(age) + ' лет')
print('Привет! Я -', name, ', мне', age, 'лет')
print('Привет! Я - ', name, ', мне ', age, ' лет', sep='')

template = 'Привет! Я - {}, мне {} лет'

print('Привет! Я - {}, мне {} лет'.format(name, age))
print('Привет! Я - {0}, мне {1} лет\n{0} ({1})'.format(name, age))
print('Привет! Я - {name}, мне {age} лет\n{name} ({age})'.format(name=name, age=age))

print(template.format(name, age))

print(f'Привет! Я - {name}, мне {age} лет')


template = 'Товар     Цена    Кол-во    Итого\n{:10}{:<6.1f}{:^10}{:7}\n{:10}{:<6.1f}{:^10}{:7}'

items = [
    ('Хлеб', 40, 1),
    ('Молоко', 105, 3),
]

print(template.format(
    items[0][0], items[0][1], items[0][2], items[0][1] * items[0][2],
    items[1][0], items[1][1], items[1][2], items[1][1] * items[1][2],
))
