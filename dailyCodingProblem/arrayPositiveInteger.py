import unittest

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def firstMissingPosInt(arr1):
    cons = 0
    arr1.sort()
    for i in range(1,len(arr1)):
        if arr1[i] >= 1:
            if arr1[i] - arr1[i-1] > 1:
                return arr1[i]-1
        if arr1[i] == arr1[-1]:
            return arr1[i]+1



class TestlistSumFind(unittest.TestCase):

    def test1(self):
        self.assertEqual(firstMissingPosInt([1, 2, 0]), 3)
    
    def test2(self):
        self.assertEqual(firstMissingPosInt([3, 4, -1, 1]), 0)
    
    def test3(self):
        self.assertEqual(firstMissingPosInt([0,3,4,5,1]), 2)

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately

