# импорт модуля из стандартной библиотеки Python,
# который генерирует случайное число
from random import randint

name_shop = 'Пятерочка'
date = '16.07.2023'

products = []
quantity = []
prices = (27.50, 49, 115, 170, 41,90)

products.append('Хлеб')
products.append('Молоко')
products.append('Сыр')
products.append('Курица')
products.append('Помидоры')

products.remove('Хлеб')
products.insert(0, 'Лаваш')


# Создадим цикл для генерации 5 случайных чисел
for lot in range(5):
    lot = randint(1, 5)
    quantity.append(lot)


sum = 0 # Переменная с итоговой суммой
total = 0 # Переменная с итоговым количеством товаров

print((' '* 32) + name_shop)
print(' '*30, 'Кассовый чек')
print('Наименование товара'+ (' '* 15) + 'Количество' + (' '* 20) + 'Цена')
print('-' * 70)

# Создаем цикл для перебора продуктов, подсчета итоговой стоимости и количества
for product in range(len(products)):
    price_product = quantity[product] * prices[product]
    print(products[product] + (' ' * 30) + str(quantity[product]) + (' ' * 30) + str(price_product))
    sum += price_product
    total += quantity[product]
print('-' * 70)
print('Итого:' + (' '* 30) + str(total) + (' '* 25) + str(sum))
print((' '*45), 'Дата покупки: ' + date)
