numbers = [1, 2, 3]
print(numbers)

a, b, c = numbers
print(c)

a, b, _ = numbers
print(b)

a, *b = numbers
print(a)
print(b)

*a, b = numbers
print(a)
print(b)

a, *_ = numbers
print(a)

numbers = [1, 2, 3, 4]
a, *_, b = numbers
print(a)
print(b)

a = [1, 2, 3]
b = [5, 6, 7]

for idx in range(len(a)):
    print(a[idx] + b[idx])

res = zip(a, b)
for pair in res:
    print(pair)
    print(pair[0] + pair[1])

res = zip(a, b)
for fst, snd in res:
    print(fst, snd)
    print(fst + snd)
