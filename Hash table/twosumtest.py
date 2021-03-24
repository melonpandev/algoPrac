import twosum
import unittest
class Test(unittest.TestCase):
    def test_examp1(self):
        nums = [2,7,11,15]
        target = 9
        assert twosum.Solution().twosum(nums,target) == [0,1] , "Wrong answer"
    def test_examp2(self):
        nums = [3,2,4]
        target = 6
        assert twosum.Solution().twosum(nums,target) == [1,2] , "Wrong answer"
    def test_examp3(self):
        nums = [3,3]
        target = 6
        assert twosum.Solution().twosum(nums,target) == [0,1] , "Wrong answer"
if __name__ == "__main__":
    unittest.main()