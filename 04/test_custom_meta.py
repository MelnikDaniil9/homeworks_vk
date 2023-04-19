import unittest
from custom_meta import CustomMeta


class TestCustomMeta(unittest.TestCase):
    def setUp(self) -> None:
        class CustomClass(metaclass=CustomMeta):
            x = 50

            def __init__(self, val=99):
                self.val = val

            def line(self):
                return 100

            def __str__(self):
                return "Custom_by_metaclass"

        self.instance_class = CustomClass()
        self.obj_class = CustomClass

    def test_class_attr(self):
        self.instance_class.dynamic = "added dynamic"
        self.instance_class.custom_dynamic = "another value"
        self.assertEqual(self.instance_class.custom_x, 50)
        self.assertEqual(self.instance_class.custom_dynamic, "added dynamic")
        self.assertEqual(self.instance_class.custom_custom_dynamic, "another value")
        with self.assertRaises(AttributeError):
            self.instance_class.x
        with self.assertRaises(AttributeError):
            self.instance_class.line()
        with self.assertRaises(AttributeError):
            self.instance_class.dynamic
        self.assertEqual(self.obj_class.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.obj_class.x
        self.instance_class.__magick__ = "magick"
        self.assertEqual(self.instance_class.__magick__, "magick")

    def test_init_attr(self):
        self.assertEqual(self.instance_class.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.instance_class.val

    def test_methods(self):
        self.assertEqual(self.instance_class.custom_line(), 100)
        self.assertEqual(str(self.instance_class), "Custom_by_metaclass")
        with self.assertRaises(AttributeError):
            self.instance_class.line()
