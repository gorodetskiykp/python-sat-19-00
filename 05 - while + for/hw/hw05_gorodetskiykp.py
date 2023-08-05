from random import randint

MIN_VALUE = 2
MAX_VALUE = 11
WIN_SCORE = 21
cards = [randint(MIN_VALUE, MAX_VALUE), randint(MIN_VALUE, MAX_VALUE)]

print(cards)

while True:
    choice = input("Ещё? ").strip().lower()
    if choice == 'нет':
        break
    elif choice == 'да':
        cards.append(randint(MIN_VALUE, MAX_VALUE))
        print(cards)
    else:
        continue

total = sum(cards)
if len(cards) > 2:
    for card in cards:
        if card == 11:
            total -= 10

if total > WIN_SCORE:
    print("Вы проиграли")
elif total < WIN_SCORE:
    print("Вы не проиграли")
elif total == WIN_SCORE:
    print("Вы выйграли")
