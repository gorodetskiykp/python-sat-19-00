from random import choice, choices

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

hand = choices(cards, k=2)
print(hand)

while sum(hand) <= 21:
    next_card = input('Ещё? (д/н) ').strip().lower()
    if next_card == 'д':
        hand.append(choice(cards))
    elif next_card == 'н':
        break
    else:
        continue
    print(hand)
    print("На руках", sum(hand))
else:
    print("Перебор!")
