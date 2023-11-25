class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __str__(self):
        return self.name


class CycleBufer:
    def __init__(self, items):
        self._size = 0
        self.current_item = None
        for item in [items[0]] + items[1:][::-1]:
            self.add(item)

    def __str__(self):
        result = [self.current_item.name]
        for _ in range(self._size - 1):
            self.current_item = self.current_item.next
            result.append(self.current_item.name)
        self.current_item = self.current_item.next
        return ', '.join(result)

    def add(self, node):
        if isinstance(node, str):
            node = Node(node)
        self._size += 1
        if self.current_item:
            node.next = self.current_item.next
            self.current_item.next = node
        else:
            self.current_item = node
            node.next = node

    def next(self):
        self.current_item = self.current_item.next


items = [Node("Tom"), Node("John"), Node("Elvis")]
bufer = CycleBufer(items)

# tom = Node("Tom")
# print(tom)

print(bufer)
print(bufer.current_item)
print(bufer.current_item.next)
print(bufer)
print(bufer.current_item)
print(bufer.current_item.next)
bufer.next()
print(bufer.current_item)
print(bufer.current_item.next)
print(bufer)
bufer.add(Node("Missi"))
print(bufer)
bufer.next()
print(bufer)
bufer.add("Hank")
print(bufer)
