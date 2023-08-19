import sys

# float - float() -> 1234.43245

print(1 / 3)
print(1 // 3)
print((0.1 + 0.1 + 0.1) == 0.3)
print(0.1 + 0.1 + 0.1)
print()
print(8.9e-2)
print(8e+2)
print()
print(sys.float_info.epsilon)
print(abs((0.1 + 0.1 + 0.1) - 0.3) <= sys.float_info.epsilon)
print()
print(float.is_integer(1.1))
print(float.is_integer(1.0))
print()
print("1.0".isdigit())
print(float("1.0"))
print()
print(float.as_integer_ratio(1.7))

