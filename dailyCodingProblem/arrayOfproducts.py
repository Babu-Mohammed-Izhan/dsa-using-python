import unittest


# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#! No division

def arrayProduct(array):
    # O(n^2)
    finalArr = []
    for i in range(len(array)):
        final = 1
        for j in range(len(array)):
            if i != j:
                final *= array[j]
        finalArr.append(final)
    return finalArr

def arrayProductFast(nums):
    # O(n)
    ans = [1]*len(nums)
    suf = 1
    pre = 1
    for i in range(len(nums)):
        ans[i] *= pre
        pre *= nums[i]
        ans[-1-i] *= suf
        suf *= nums[-1-i]
    return ans


class TestlistSumFind(unittest.TestCase):

    def test1(self):
        self.assertEqual(arrayProductFast([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    
    def test2(self):
        self.assertEqual(arrayProduct([3, 2, 1]), [2, 3, 6])

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately