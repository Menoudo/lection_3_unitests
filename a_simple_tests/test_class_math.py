import unittest


class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.x = 1
        self.y = 2

    def tearDown(self):
        # TODO document why this method is empty
        pass

    def test_addition(self):
        result = self.x + self.y
        self.assertEqual(result, 3)

    def test_subtraction(self):
        result = self.x - self.y
        self.assertEqual(result, -1)
