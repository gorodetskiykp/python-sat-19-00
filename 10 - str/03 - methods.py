# Методы строк

text = 'hello World !'

print(dir(text))

"""
, 'center', 'encode', , 'expandtabs', 
', 'format_map',,, 
, 'isidentifier', ,  'isprintable', 'isspace'
, ,  'ljust', , 'maketrans', 
'partition',,, 
'rjust', 'rpartition', ,  'splitlines', , 
, , 'translate', 'zfill'
"""

# Регистры
"""
'capitalize'
'title'
'lower'
'upper'
'casefold'
'swapcase'

'istitle'
'islower'
'isupper'
"""

print(text.capitalize())  # Hello world!
print(text.title())  # Hello World!
print("i'm python".title())  # I'M Python
print(text.lower())  # hello world!
print(text.upper())  # HELLO WORLD!
print(text.casefold())  # hello world!
print(text.swapcase())  # HELLO wORLD!


# Преоброзования строк - удаление/замена элементов
"""
'strip'
'rsplit'
'lstrip'
'replace'
'removeprefix'
'removesuffix'
"""

text = '     \tHello World\n   \n'
print(text.strip())  # Hello World

text = 'hello World!'
print(text.replace('h', 'H'))  # Hello World!

text = '     \thello        world\n   \n'
print(text.replace('h', 'H').replace('w', 'W').strip())
print(text.replace('h', 'H').replace('w', 'W').strip().replace("  ", " ")
      .replace("  ", " ").replace("  ", " "))

text = 'hello! World!'
print(text.replace('h', 'H').removesuffix('!'))  # Hello World!


# СЧЁТ ЭЛЕМЕНТОВ - count

text = 'hello! World!'
print(text.count('l'))  # 3

# ПРОВЕРКИ

"""
'startswith'
'endswith'
'isalnum'
'isalpha'
'isascii'
'isdecimal'
'isdigit'
'isidentifier'
'isnumeric'
'isprintable'
'isspace'
"""

text = 'hello! World!'
print(text[-1] == '!')  # True
print(text.endswith('!'))  # True

print("12".isdigit())  # True
print("12".isnumeric())  # True
print("hello".isalpha())  # True
print("hello12".isalnum())  # True

# ПОИСК

"""
'index'
'find'
'rindex'
'rfind'
"""

text = 'hello! World!'
print(text.index('!'), text.find('!'))  # 5 5
print(text.index('!', 6), text.find('!', 6))  # 12 12

# print(help(str.index))
# print(text.index('?')) -> ValueError: substring not found
if '?' in text:
    print(text.index('?'))
else:
    print('No ?')

result = text.find('?')
print(result)  # -1
if result == -1:
    print('No ?')
