numbers = [1, 2, 11, 10, 22, 21]
print(sorted(numbers))
numbers.sort()
print(numbers)

numbers = [1, 2, 11, 10, 22, 21]
print(sorted(numbers, reverse=True))
numbers.sort(reverse=True)
print(numbers)

numbers = ["1", "2", "11", "10", "22", "21"]
print(sorted(numbers, key=int))
numbers.sort(key=int)
print(numbers)

# print(ord("1"))  # 49
# print(ord("2"))  # 50
# print(ord("a"))  # 97
# print(ord("A"))  # 65
#
# print("a" > "A")  # True


def even(item):
    if int(item) % 2 == 0:
        return 0, int(item)
    else:
        return 1, int(item)


numbers = ["21", "1", "2", "11", "10", "22", "100"]

print(sorted(numbers, key=even))
numbers.sort(key=even)
print(numbers)
