import unittest


arr = [3, 9, 13, 7]
k = 8

def two_sum (array , n):
    for idx,i in enumerate(array):
        for jdx,j in enumerate(array):
            if idx == jdx:
                break
            if i+j == n:
                return True
    return False


class TestTwoSum(unittest.TestCase):

    def test1(self):
        self.assertEqual(two_sum([1, 3, 8, 2],10), True)
    
    def test2(self):
        self.assertEqual(two_sum([3, 9, 13, 7],8), False)
    
    def test3(self):
        self.assertEqual(two_sum([4, 2, 6, 5, 2],4), True)

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately