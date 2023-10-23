# int, bool, float, str
# str - 'hello', tuple - (1, 2, 3), list - [1, 2, 'hello']

# коллекции - col[idx], len(), item in col

# Словари
# car_color = values[5][0]

colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
colors_list = ['#FF0000', '#00FF00', '#0000FF']

colors_list[0]  # '#FF0000'
colors['red']  # '#FF0000'


# создание словаря
some_dict = {}
some_dict = dict()
some_dict = dict([('k1', 'v1'), (1, 2), ((4, 5, 6), [7, 8, 9])])
# {'k1': 'v1', 1: 2, (4, 5, 6): [7, 8 ,9]}

colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}

# Методы словаря

# get()
colors['red']  # '#FF0000'
colors['black']  # Ошибка - KeyError

colors.get('red')  # '#FF0000'
colors.get('black')  # None

if 'black' in colors:  # поиск в ключах
    print(colors['black'])
else:
    print(None)

colors.get('red', 'blank')  # '#FF0000'
colors.get('black', 'blank')  # 'blank'

# fromkeys()
keys = [1, 2, 3, 4]
sq_dict = some_dict.fromkeys(keys)  # {1: None, 2: None, 3: None, 4: None}
sq_dict = some_dict.fromkeys(keys, 0)  # {1: 0, 2: 0, 3: 0, 4: 0}
sq_dict[1] = 6  # {1: 6, 2: 0, 3: 0, 4: 0}

sq_dict = some_dict.fromkeys(keys, [])  # {1: [], 2: [], 3: [], 4: []}
sq_dict[1].append[6]  # {1: [6], 2: [6], 3: [6], 4: [6]}

# Добавление данных
colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
colors['black'] = '#000000'
# {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'black': '#000000'}

for item in [1, 2, 3]:  # item <- list_value
    pass

for item in {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}:
    pass  # item <- key


colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
for item in colors:
    print(item)  # 'red'

for item in colors.keys():
    print(item)  # 'red'
    print(colors[item])  # '#FF0000'
    print(colors.get(item))  # '#FF0000'

for item in colors.values():
    print(item)  # '#FF0000'

for item in colors.items():
    print(item)  # ('red', '#FF0000')
    print(item[0])  # 'red'
    print(item[1])  # '#FF0000'

for color_name, color_hex in colors.items():
    print(item)  # ('red', '#FF0000')
    print(color_name)  # 'red'
    print(color_hex)  # '#FF0000'

colors1 = colors

# 'pop', 'popitem', 'setdefault', 'update' - ДЗ
