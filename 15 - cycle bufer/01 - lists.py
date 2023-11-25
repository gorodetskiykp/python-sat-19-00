# tuple, list, set, dict


def next(items: list[str], current_item_index: int) -> int:
    next_item_index = (current_item_index + 1) % len(items)
    return next_item_index


items = ["Tom", "John", "Elvis"]
current_item_index = 0
current_item = items[current_item_index]
print(current_item)

for _ in range(10):
    current_item_index = next(items, current_item_index)
    current_item = items[current_item_index]
    print(current_item)
