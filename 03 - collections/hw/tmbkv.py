SHOP_NAME = 'Шестерочка'
DATA = '19.07.2023 г.'

name = []
quantity = []
price = []

name.append('Батон')
name.append('Молоко')
name.append('Яйца')

quantity.append(1)
quantity.append(2)
quantity.append(3)

price.append(50)
price.append(100)
price.append(150)

name.remove('Яйца')
name.insert(2, 'Кефир')

print(
    'Кассовый чек', '\n'
    '\n',
    'Магазин', SHOP_NAME, '\n'
    'Дата покупки', DATA, '\n'
    'Наименование;', 'Количество, шт.;', 'Цена, руб.;', 'Итого, руб.:', '\n',
    name[0], ',', quantity[0], ',', price[0], ',', quantity[0]*price[0], '\n',
    name[1], ',', quantity[1], ',', price[1], ',', quantity[1]*price[1], '\n',
    name[2], ',', quantity[2], ',', price[2], ',', quantity[2]*price[2], '\n',
    '\n',
    'Всего наименований:', len(name), 'шт.', '\n',
    'Итого, общая сумма счета:', (quantity[0]*price[0])+(quantity[1]*price[1])+(quantity[2]*price[2]), 'руб.' '\n',
)