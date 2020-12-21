import unittest
from app import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cl = Solution()
        self.assertEqual('a', cl.longestPalindrome('abcd'))
        self.assertEqual('aca', cl.longestPalindrome('acab'))
        self.assertEqual('ff', cl.longestPalindrome('dff'))
        self.assertEqual('a', cl.longestPalindrome('a'))
        self.assertEqual('aca', cl.longestPalindrome('aacabdkacaa'))


if __name__ == '__main__':
    unittest.main()
