# Списковые включения плюс условия

numbers = [1, 5, 7, 4]
result = []

for number in numbers:
    if number % 2 == 1:
        result.append(number ** 2)

print(result)

# создаём результирующий список
# запускаем цикл
# складываем результат опрерации над очередным элментом в результирующий список
# в случае выполнения условий

result2 = [number ** 2 for number in numbers if number % 2 == 1]
print(result2)
