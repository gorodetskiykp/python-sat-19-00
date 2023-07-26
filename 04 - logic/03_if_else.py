# if УСЛОВИЕ (True/False):
#    ОПЕРАЦИЯ 1 если УСЛОВИЕ True
#    ОПЕРАЦИЯ 2 если УСЛОВИЕ True
#    ОПЕРАЦИЯ 3 если УСЛОВИЕ True

apples = 5

if apples > 0:
    print('i eat 1st apple')
    print('i eat 2nd apple')
    print('i eat 3rd apple')

print('the end')

# if УСЛОВИЕ (True/False):
#    ОПЕРАЦИЯ 1 если УСЛОВИЕ True
#    ОПЕРАЦИЯ 2 если УСЛОВИЕ True
#    ОПЕРАЦИЯ 3 если УСЛОВИЕ True
# else:
#    ОПЕРАЦИЯ 4 если УСЛОВИЕ False
#    ОПЕРАЦИЯ 5 если УСЛОВИЕ False
#    ОПЕРАЦИЯ 6 если УСЛОВИЕ False

if apples > 0:
    print('i eat 1st apple')
    print('i eat 2nd apple')
    print('i eat 3rd apple')
else:
    print('i want an apple')

print('the end')


# if УСЛОВИЕ1 (True/False):
#    ОПЕРАЦИЯ 1 если УСЛОВИЕ1 True
#    ОПЕРАЦИЯ 2 если УСЛОВИЕ1 True
#    ОПЕРАЦИЯ 3 если УСЛОВИЕ1 True
# elif УСЛОВИЕ2 (True/False):
#    ОПЕРАЦИЯ 1 если УСЛОВИЕ2 True
#    ОПЕРАЦИЯ 2 если УСЛОВИЕ2 True
#    ОПЕРАЦИЯ 3 если УСЛОВИЕ2 True
# else:
#    ОПЕРАЦИЯ 4 если УСЛОВИЕ1 False и УСЛОВИЕ2 False
#    ОПЕРАЦИЯ 5 если УСЛОВИЕ1 False и УСЛОВИЕ2 False
#    ОПЕРАЦИЯ 6 если УСЛОВИЕ1 False и УСЛОВИЕ2 False

age = 2

if age < 3:
    print("price 0")
elif age < 10:
    print("price 50%")
else:
    print("full price")
