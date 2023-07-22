staff_list = []  # список товаров в чеке

staff_list.append('Вкусный и полезный кормушек, дорогой жаль')
staff_list.append('Наполнитель в туалет, пахнет вкусненько, лучше ёлочки')
staff_list.append('Мышь игрушечная, шуршит, покусывать приятно можно')
staff_list.append('Когтеточка картонная, удобно и спать, и чесать')
staff_list.append('Колбаса со стола, вредно, не надо')

staff_list.remove('Колбаса со стола, вредно, не надо')
staff_list.insert(3, 'Молоко, так и быть, можно, но немножко')

price_list = []  # стоимость товаров в чеке

price_list.append(1700)
price_list.append(620)
price_list.append(135)
price_list.append(85)
price_list.append(315)

# общая стоимость товаров, чтобы в print не добавлять 100 раз этого монстра
amount = (price_list[0]+price_list[1] + price_list[2] + price_list[3]
          + price_list[4])
# amount = sum(price_list)

shop = 'Cat Space'  # название магазина
time = '19.07.2023'  # дата продажи
seller_name = 'Хлызова Д.М.'  # имя кассира

# линия для красоты
line = '---------------------------------------------------------'
# line = '-' * 57

print('                     ООО ', shop, '\n',
      '                 Кассир: ', seller_name, '\n',
      line, '\n',
      '1. ', staff_list[0], '\n',
      'Стоимость: ', price_list[0], '\n',
      '2. ', staff_list[1], '\n',
      'Стоимость: ', price_list[1], '\n',
      '3. ', staff_list[2], '\n',
      'Стоимость: ', price_list[2], '\n',
      '4. ', staff_list[3], '\n',
      'Стоимость:', price_list[3], '\n',
      '5. ', staff_list[4], '\n',
      'Стоимость:', price_list[4], '\n',
      line, '\n',
      'Всего: ', amount, '\n',
      time, '                                 ', seller_name, '\n',
      line, '\n',
      'ИТОГ: ', amount, '\n',
      'НАЛИЧНЫМИ: ', amount, '\n',
      '                   Спасибо за визит! :з'
      )
