petia_apples = 5
ivan_apples = 7

print(petia_apples > ivan_apples)  # False >
print(petia_apples < ivan_apples)  # True <
print(petia_apples >= ivan_apples)  # False > =
print(petia_apples <= ivan_apples)  # True < =
print(petia_apples == ivan_apples)  # False = =
print(petia_apples != ivan_apples)  # True ! =

print(0 < petia_apples <= 10)  # True
# print(0 > petia_apples <= 10)  - BAD LOGIC

# логические операторы - and, or, not
print(petia_apples > 0 and petia_apples <= 10)  # True
print(petia_apples > 0 and ivan_apples > 0)  # True
print(petia_apples > 0 or ivan_apples > 0)  # True

print(petia_apples != 5)  # False
print(not (petia_apples == 5))  # False

# Таблицы истинности
# a b and or not_a
# 0 0  0   0  1
# 0 1  0   1  1
# 1 0  0   1  0
# 1 1  1   1  0


number = "7"

number = int(number) % 3  # 7 % 3 OR ERROR

if number.isdigit() and int(number) % 3 == 1:
    pass


# Оператор членства - in
# Коллекции: str, list, tuple

print(7 in [1, 2, 3, 7, 8])  # True
print("hello" in "hello world")  # True
