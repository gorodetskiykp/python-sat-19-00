store_name = 'пятак'
data = '18.07.2023'

name_products = []
how_many = []
price = []

name_products.append('хлеб')
how_many.append(1)
price.append(39)

name_products.append('молоко')
how_many.append(2)
price.append(43)

name_products.append('масло')
how_many.append(1)
price.append(25)

name_products.remove('масло')
name_products.insert(0, 'сыр')
price.remove(25)
price.insert(0, 70)

total = sum(how_many * price for how_many, price in zip(how_many, price))

print("-------------------------------")
print(f"             {store_name:}")
print("-------------------------------")
print(f"Дата:   {data}")
print("-------------------------------")
print("Товар        Кол-во        Цена")
print("-------------------------------")

for name_product, how_many, price in zip(name_products, how_many, price):

    print(f"{name_product:15} {how_many:1}   {price:11.2f}")

print("-------------------------------")
print(f"Итого: {total:.2f} руб.")
print("-------------------------------")
