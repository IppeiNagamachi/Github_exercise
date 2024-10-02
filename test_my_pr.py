import unittest
from my_pr import func_for_PR

class TestMyPR(unittest.TestCase):
    def test_func_for_PR(self):
        self.assertEqual(func_for_PR(10, 20), 30)
        self.assertEqual(func_for_PR(-10, 10), 0)
        self.assertEqual(func_for_PR(0, 0), 0)

if __name__ == '__main__':
    unittest.main()