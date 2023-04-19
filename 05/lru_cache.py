class LRUCache:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

        def add_node(self, node):
            next_node = self.next
            self.next = node
            node.prev = self
            node.next = next_node
            next_node.prev = node

        def remove_node(self):
            prev_node = self.prev
            next_node = self.next
            prev_node.next = next_node
            next_node.prev = prev_node

    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        node.remove_node()
        self.head.add_node(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.remove_node()
            self.head.add_node(node)
        else:
            if key is not None:
                if len(self.cache) == self.limit:
                    prev_tail = self.tail.prev
                    prev_tail.remove_node()
                    del self.cache[prev_tail.key]
                node = self.Node(key, value)
                self.cache[key] = node
                self.head.add_node(node)
