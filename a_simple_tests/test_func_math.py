import unittest


class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div = 1 / 0
