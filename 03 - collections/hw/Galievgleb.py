# Название магазина и дата
shop_name = "Магазин 'Пятерочка'"
date = "18.07.2023"

# Создание списков для товаров, их количества и цены
products = []
count = []
prices = []

# Добавление данных в списки
products.append("Яблоки")
count.append(3)
prices.append(50.0)

products.append("Молоко")
count.append(2)
prices.append(80.0)

products.append("Хлеб")
count.append(1)
prices.append(30.0)

# Изменение данных в списках
products.remove("Молоко")
products.insert(1, "Сыр")

# Вычисление итоговой суммы
total = sum(count * price for count, price in zip(count, prices))

# Печать чека
print("-------------------------------")
print(f"      {shop_name}")
print("-------------------------------")
print(f"Дата: {date}")
print("-------------------------------")
print("Товар           Кол-во   Цена")
print("-------------------------------")

for product, count, price in zip(products, count, prices):
    # Используем цикл for и функцию zip для итерации по товарам, количеству и цене одновременно.

    print(f"{product:15} {count:5}   {price:5.2f}")

print("-------------------------------")
print(f"Итого: {total:.2f} руб.")
print("-------------------------------")
