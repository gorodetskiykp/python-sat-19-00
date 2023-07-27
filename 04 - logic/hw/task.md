# Домашнее задание

## Предусловия

- сдаем пул-реквестами
- потребуется функция randint\
подключается в первых строчках программы следующим образом:
```from random import randint```
- использование: ```number = radnint(1, 100)``` - генерирует случайное число в 
диапазоне от 1 до 100 (включительно)
- ещё потребуется функция ```input()```
- используется следующим образом:
```choice = input("Сделайте свой выбор: ")``` - в консоли появится приглашение
на ввод данных
- учтите, что в переменной ```choice``` будут лежать данные в сроковом виде 
(тип - ```str```) - если нужно число, не забудьте преобразовать ```choice``` функцией 
```int()```

## Задание - игра "21"
1. Выдать пользователю две случайные карты (номинал - от 2 до 11)
2. Спросить, нужна ли еще карта
3. Если ДА - выдать ещё одну случайную карту и перейти к подсчёту результата
4. Если НЕТ - сразу перейти к подсчёту результата 
5. Если на руках 3 карты, номинал 11 заменить на номинал 1
6. Если сумма номиналов меньше 21 - написать ВЫ НЕ ПРОИГРАЛИ
7. Если сумма номиналов ровно 21 - написать ВЫ ВЫЙГРАЛИ
8. Если сумма номиналов больше 21 - написать ВЫ ПРОИГРАЛИ