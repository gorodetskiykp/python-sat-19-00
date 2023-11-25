class CycleBufer:
    def __init__(self, items):
        self._items = items
        self._current_item_index = 0
        self.current_item = self._items[self._current_item_index]
        self._next_item_index = self._next()
        self.next_item = self._items[self._next_item_index]

    def __str__(self):
        return ', '.join(self._items)

    def _next(self):
        return (self._current_item_index + 1) % len(self._items)

    def _set_current_item(self, item_index):
        self._current_item_index = item_index
        self.current_item = self._items[self._current_item_index]
        self._next_item_index = self._next()
        self.next_item = self._items[self._next_item_index]

    def go_next(self):
        self._set_current_item(self._next())

    def add(self, item):
        if self._current_item_index == len(self._items) - 1:
            self._items.append(item)
        else:
            self._items.insert(self._next(), item)
        self.next_item = item


items = CycleBufer(["Tom", "John", "Elvis"])
print(items)
print(items.current_item)
print(items.next_item)
items.go_next()
print(items.current_item)
print(items.next_item)
print(items)
items.add('Morty')
print(items)
print(items.current_item)
print(items.next_item)
items.go_next()
items.go_next()
print()
print(items.current_item)
print(items.next_item)
items.add('Jina')
print(items)
print(items.current_item)
print(items.next_item)
items.go_next()
print(items.current_item)
print(items.next_item)
