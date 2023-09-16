# СРЕЗЫ

text = 'Hello World!'
# | H | e | l | l | o |  | W | o | r | l | d | ! |
print(text[6:11])  # World
print(text[0:5])  # Hello
print(text[:5])  # Hello
print(text[6:2000])  # World!
print(text[6:])  # World!
print(text[:])  # Hello World!
# print(text[100]) -> ERROR

print(text[6:11:1])  # World
print(text[6:11:2])  # Wrd

print(text[::2])  # HloWrd
print(text[::-1])  # !dlroW olleH

print(text[-2:-7:-1])  # dlroW

print(text[6:11][::-1])  # dlroW
