from datetime import datetime  # импорт модуля даты

shop_list = []
shop_list.append("Coca Cola Zero")
shop_list.append("Апельсины вес.")
shop_list.append("Жеват. конфеты Мамба")
shop_list.append("Креветки замороженные вес.")
shop_list.append("Паста \"Свежеготово\" 200гр")
shop_list.remove("Паста \"Свежеготово\" 200гр")
shop_list.insert(4, "Наггетсы для жарки 350 гр.")
shop_name = "Магазин SPAR Томск, ул. проспект Фрунзе 109"
date = datetime.now().date()
# список с количеством единиц товара и ценой единицы по каждому наименованию
price_list = [[1, 300], [0.597, 290], [1, 74], [1.124, 785], [1, 170]]

summary = 0  # Переменная для подсчета ИТОГО
i = 0

print("                    АТОЛ                    \n",
      "", shop_name, "\n"
      "                ", date, "\n")

while i < len(shop_list):
    # Проверяем количество единиц товара, чтобы указать шт. или кг.
    if type(price_list[i][0]) == float:
        print(shop_list[i], "-", price_list[i][0],"кг.",
            "\n........................................", price_list[i][0]*price_list[i][1])
    elif type(price_list[i][0]) == int:
        print(shop_list[i], "-", price_list[i][0],"шт.",
            "\n........................................", format(price_list[i][0]*price_list[i][1],".2f"))
    summary = summary + price_list[i][0] * price_list[i][1]  # сразу считаем итоговую сумму
    i=i+1

print("\nИТОГО .................................", summary, "\n"
      "\n Кассир: Крутой Уокер"
      "\n Спасибо, что выбираете нас!")