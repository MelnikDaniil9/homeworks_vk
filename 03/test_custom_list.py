import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def test_add_radd(self):
        self.assertEqual(CustomList([1, 2]) + CustomList([1]), CustomList([2, 2]))
        self.assertEqual(
            CustomList([1, 2]) + CustomList([1, 2, 3]), CustomList([2, 4, 3])
        )
        self.assertEqual(CustomList([-3, 2]) + CustomList([1]), CustomList([-2, 2]))
        self.assertEqual([1, 2] + CustomList([1]), CustomList([2, 2]))
        self.assertEqual([1, 2] + CustomList([1, 2, 3]), CustomList([2, 4, 3]))
        self.assertEqual(CustomList([1, 2]) + [0, -2, 1], CustomList([1, 0, 1]))

    def test_sub_rsub(self):
        self.assertEqual(CustomList([1, 2]) - CustomList([1]), CustomList([0, 2]))
        self.assertEqual(
            CustomList([1, 2]) - CustomList([1, 2, 3]), CustomList([0, 0, -3])
        )
        self.assertEqual(CustomList([-3, 2]) - CustomList([1]), CustomList([-4, 2]))
        self.assertEqual([1, 2] - CustomList([1]), CustomList([0, 2]))
        self.assertEqual([1, 2] - CustomList([1, 2, 3]), CustomList([0, 0, -3]))
        self.assertEqual(CustomList([1, 2]) - [0, -2, 1], CustomList([1, 4, -1]))

    def test_eq_ne(self):
        self.assertTrue(CustomList([1, 2, 3]) == CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) == [1, 2, 3])
        self.assertFalse(CustomList([1, 2]) == CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) != CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2]) != [1, 2, 3])
        self.assertTrue(CustomList([1, 2]) != CustomList([1, 2, 3]))

    def test_le_lt(self):
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) <= [1, 2, 3])
        self.assertTrue(CustomList([1, 2]) < CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2]) < [1, 2, 3])
        self.assertTrue(CustomList([1, 2]) <= CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) < CustomList([1, 2]))
        self.assertFalse(CustomList([1, 2, 3]) <= CustomList([1, 2]))

    def test_ge_gt(self):
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) >= [1, 2, 3])
        self.assertTrue(CustomList([1, 2, 3]) > CustomList([1, 2]))
        self.assertFalse(CustomList([1, 2, 3]) > [1, 2])
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([1, 2]))
        self.assertFalse(CustomList([1, 2]) > CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2]) >= CustomList([1, 2, 3]))

    def test_str(self):
        self.assertEqual(str(CustomList([1, 2, 3])), "Elems: [1, 2, 3]\nSum: 6")
        self.assertEqual(repr(CustomList([1, 2, 3])), "Elems: [1, 2, 3]\nSum: 6")
