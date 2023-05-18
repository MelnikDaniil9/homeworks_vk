import logging
import sys


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

        logging.basicConfig(filename="cache.log", level=logging.DEBUG)
        self.logger = logging.getLogger("LRUCache")

        # Создание обработчика для уровня DEBUG
        debug_handler = logging.FileHandler("debug.log")
        debug_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(debug_handler)

        # Создание обработчика для уровня INFO
        info_handler = logging.FileHandler("info.log")
        info_handler.setLevel(logging.INFO)
        self.logger.addHandler(info_handler)

        if "-s" in sys.argv:
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(stdout_handler)

        if "-f" in sys.argv:
            self.logger.addFilter(CustomFilter())

    def get(self, key):
        if key not in self.cache:
            self.logger.debug(f"Key '{key}' not found in cache")
            return None
        node = self.cache[key]
        node.remove_node()
        self.head.add_node(node)
        self.logger.debug(f"Got value '{node.value}' for key '{key}' from cache")
        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.remove_node()
            self.head.add_node(node)
            self.logger.debug(f"Updated value for key '{key}' in cache")
        else:
            if key is not None:
                if len(self.cache) == self.limit:
                    prev_tail = self.tail.prev
                    prev_tail.remove_node()
                    del self.cache[prev_tail.key]
                    self.logger.debug(
                        f"Cache limit reached. Evicted key '{prev_tail.key}'"
                    )
                node = self.Node(key, value)
                self.cache[key] = node
                self.head.add_node(node)
                self.logger.debug(f"Added key-value pair '{key}':'{value}' to cache")
                self.logger.info(f"Set key-value pair '{key}':'{value}' in cache")


class CustomFilter(logging.Filter):
    def filter(self, record):
        return len(record.getMessage().split()) % 2 != 0


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set("key1", "one")
    cache.set("key2", "two")
    cache.set("key3", "three, four")
    cache.get(2)
    cache.get(4)
    cache.set("key4", "four")
