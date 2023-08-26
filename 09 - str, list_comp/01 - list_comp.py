# Списковые включения

numbers = [1, 5, 7, 4]
result = []

for number in numbers:
    result.append(number ** 2)

print(result)

# создаём результирующий список
# запускаем цикл
# складываем результат опрерации над очередным элментом в результирующий список

result2 = [number ** 2 for number in numbers]
print(result2)
