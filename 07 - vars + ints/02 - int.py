number = 1
print(type(number))

print(int("123") + 5)
print(int(123.56) + 5)
print()

# dec - 1, 2, 3
# bin() - 0b1, 0b10, 0b11
# oct() - 0o1, 0b2, 0o3
# hex() - 0x1, 0x2, 0x3, ..., 0xF

print(0b010111010111)
print(bin(1495))

number = '45F'
print(int(number, 16))

# получение абсолютного значение
print(abs(-56))

num1 = 11
num2 = 3
print(num1 // num2)
print(num1 % num2)
print(divmod(num1, num2))
print(num1 ** num2)
print(pow(num1, num2))
print(round(num1 / num2, 2))

# True and False -> False

# 0 | 1 -> 1 # или, сложение
# 1 | 1 -> 1 # или
# 1 | 0 -> 1 # или
# 0 | 0 -> 0 # или

print(12 | 14)
print(bin(12))
print(bin(14))

# 1 ^ 0 - исключающее или
# 1 & 0 - и, умножение
# -1
# >>
# <<

print(2 << 2)
