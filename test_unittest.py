# https://instabyte.io/p/interview-master-100
# https://www.youtube.com/watch?v=-PHBRzL80Lk
import unittest   # The test framework
import recursion    # The code to test 25: Number of 1 Bits https://leetcode.com/problems/number-of-1-bits/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(recursion.countSetBits(5), 2)

if __name__ == '__main__':
    unittest.main()
