def get_min_card(hand: list, tramp_mark: str):
    new_hand = []
    for card in hand:
        if tramp_mark not in card:
            new_hand.append(card)
    return min(new_hand)
print(get_min_card(hand, tramp_mark))

