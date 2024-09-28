import unittest
from b_unittests.my_math import multiply


class TestMathOperations(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 5), -5)
