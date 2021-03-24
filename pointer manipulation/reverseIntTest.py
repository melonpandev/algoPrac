import reverseint
import unittest
class Test(unittest.TestCase):
    def test_examp1(self):
        target = 123
        assert reverseint.Solution().reverse(target) == 321 , "Wrong answer"
    def test_zero(self):
        target= 0
        assert reverseint.Solution().reverse(target) == 0 , "Wrong answer"
    def test_lowerbound(self):
        target = -9463847412
        assert reverseint.Solution().reverse(target) == 0 , "Wrong answer"
    def test_upperbound(self):
        target = 8463847412
        assert reverseint.Solution().reverse(target) == 0 , "Wrong answer"

if __name__ == "__main__":
    unittest.main()