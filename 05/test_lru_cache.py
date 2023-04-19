import unittest
from lru_cache import LRUCache


class TestCustomMeta(unittest.TestCase):
    def setUp(self) -> None:
        self.cache = LRUCache(3)

    def test_not_existent(self):
        self.assertEqual(self.cache.get("non_existent_key"), None)

    def test_correct_update(self):
        self.cache.set("key1", "value1")
        self.cache.set("key2", "value2")
        self.cache.set("key1", "new_value")
        self.assertEqual(self.cache.get("key1"), "new_value")

    def test_remove_order(self):
        self.cache.set("key1", "value1")
        self.cache.set("key2", "value2")
        self.cache.set("key3", "value3")
        self.cache.get("key1")
        self.cache.set("key4", "value4")
        self.assertEqual(self.cache.get("key2"), None)

    def test_cache_overflow(self):
        self.cache.set("key1", "value1")
        self.cache.set("key2", "value2")
        self.cache.set("key3", "value3")
        self.cache.set("key4", "value4")
        self.assertEqual(self.cache.get("key1"), None)

    def test_key_update(self):
        self.cache.set("key1", "value1")
        self.cache.set("key2", "value2")
        self.cache.set("key3", "value3")
        self.cache.set("key1", "new_value")
        self.assertEqual(len(self.cache.cache), 3)

    def test_invalid_key(self):
        with self.assertRaises(TypeError):
            self.cache.set(["key"], "value1")
        with self.assertRaises(TypeError):
            self.cache.set({"key": "val"}, "value1")
        with self.assertRaises(TypeError):
            self.cache.set({1, 2, 3}, "value1")
        self.cache.set(None, "value1")
        self.assertEqual(len(self.cache.cache), 0)
