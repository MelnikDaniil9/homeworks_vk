import unittest
from descriptor import Integer, String, PositiveInteger


class TestDescriptors(unittest.TestCase):
    def setUp(self) -> None:
        class Data:
            integer = Integer()
            string = String()
            positive_int = PositiveInteger()

            def __init__(self, num, name, price):
                self.integer = num
                self.string = name
                self.positive_int = price

        self.data = Data

    def test_integer(self):
        self.assertEqual(self.data.integer, None)
        data_instance = self.data(42, "test", 10)
        self.assertEqual(data_instance.integer, 42)
        with self.assertRaises(TypeError):
            data_instance.integer = "42"
        self.assertEqual(data_instance.integer, 42)
        data_instance.integer = 300
        self.assertEqual(data_instance.integer, 300)
        del data_instance.integer
        with self.assertRaises(AttributeError):
            data_instance.integer

    def test_string(self):
        self.assertEqual(self.data.string, None)
        data_instance = self.data(42, "test", 10)
        self.assertEqual(data_instance.string, "test")
        with self.assertRaises(TypeError):
            data_instance.string = 42
        self.assertEqual(data_instance.string, "test")
        data_instance.string = "300"
        self.assertEqual(data_instance.string, "300")
        del data_instance.string
        with self.assertRaises(AttributeError):
            data_instance.string

    def test_positive_int(self):
        self.assertEqual(self.data.positive_int, None)
        data_instance = self.data(42, "test", 10)
        self.assertEqual(data_instance.positive_int, 10)
        with self.assertRaises(TypeError):
            data_instance.positive_int = "42"
        with self.assertRaises(TypeError):
            data_instance.positive_int = -0.5
        self.assertEqual(data_instance.positive_int, 10)
        data_instance.positive_int = 300
        self.assertEqual(data_instance.positive_int, 300)
        del data_instance.positive_int
        with self.assertRaises(AttributeError):
            data_instance.positive_int
