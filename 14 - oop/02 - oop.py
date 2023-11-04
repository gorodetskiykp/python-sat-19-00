# шаблон - класс / тип
# экземпляр/инстанс - объект

# Type/Object

# snake_case
# CamelCase

# Инкапсуляция
# Наследование
# Полиморфизм


class Car:
    def __init__(self):
        self.color = 'black'
        self.mark = 'Toyota'

    def __str__(self):
        return "Машина"


my_car = Car()
your_car = Car()

print(my_car)
print(your_car)
print(my_car.color)
print(your_car.color)
my_car.color = 'red'
print(my_car.color)

print(dir(my_car))
# print(dir(list))

# print(my_car.__str__())
