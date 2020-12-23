import unittest
from app import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        t = Solution()
        self.assertEqual(21, t.nextGreaterElement(12))
        self.assertEqual(-1, t.nextGreaterElement(21))
        self.assertEqual(213, t.nextGreaterElement(132))
        self.assertEqual(-1, t.nextGreaterElement(9999))
        self.assertEqual(58898, t.nextGreaterElement(58889))
        self.assertEqual(-1, t.nextGreaterElement(2**32))


if __name__ == '__main__':
    unittest.main()
