
hand = ['1K', '3B', '2H', '4C', '5K', '6K']
tramp_mark = 'K'
new_hand = []

def get_min_card(hand):
    for i in hand:
        if tramp_mark in i:
            continue
        else:
            new_hand.append(i)
    return min(new_hand)
print(get_min_card(hand))

