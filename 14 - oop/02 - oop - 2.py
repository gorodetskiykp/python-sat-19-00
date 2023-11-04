class Car:
    def __init__(self, color='black', mark='VAZ'):
        self.color = color
        self.mark = mark
        self.speed = 0
        self.engine_limit = 100

    def __str__(self):
        return 'Машина - {}, {}'.format(self.color, self.mark)

    def __eq__(self, other):
        return self.speed == other.speed

    def __gt__(self, other):
        return self.speed > other.speed

    def __add__(self, other):
        return Car(color=self.color+other.color, mark=self.mark+other.mark)

    def speed_up(self, speed=2):
        if self.speed < 200:
            if self.engine_limit > 70:
                self.speed += speed
            else:
                self.speed += speed * 0.5
        if self.speed == 200:
            self.engine_limit *= 0.99999999


my_car = Car('blue', 'Haval')

print(my_car)
print(Car(mark='UAZ', color='military-green'))

devil_car = Car(mark='UAZ', color='military-green')

print(my_car.speed)
my_car.speed_up()
print(my_car.speed)
my_car.speed = 180  # BAD !!
print(my_car.speed)
# Car.speed_up(my_car)
# print(my_car.speed)
my_car.speed_up()
print(my_car.speed)
my_car.speed_up()
print(my_car.speed)
my_car.speed_up()
print(my_car.speed)

print(my_car == devil_car)
print(my_car > devil_car)
print(my_car < devil_car)

crash = my_car + devil_car
print(crash)
