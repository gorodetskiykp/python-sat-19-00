# однострочные условия

eggs = 1

what_to_do = ''
if eggs > 2:
    what_to_do = 'Делаем яичницу'
else:
    what_to_do = 'Пьем кофе'

print(what_to_do)

what_to_do = 'Делаем яичницу' if eggs > 2 else 'Пьем кофе'
print(what_to_do)
