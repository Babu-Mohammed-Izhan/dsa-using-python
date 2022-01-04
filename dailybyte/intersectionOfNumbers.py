import unittest

#  Given two integer arrays, return their intersection.
# Note: the intersection is the set of elements that are common to both arrays.

# Ex: Given the following arrays...

# nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
# nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
# nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []

def intersectionOfNum(nums1, nums2):

    #O(n)

    nums = {}
    final = set()
    if len(nums1) >= len(nums2):
        #O(2n) = O(n)
        for i in nums1:
            nums[i] = i
        for k in nums2:
            if k in nums.keys():
                final.add(k)
    else:
        #O(2n) = O(n)
        for j in nums2:
            nums[j] = j
        for k in nums1:
            if k in nums.keys():
                final.add(k)

    return list(final)



class JewelsStones(unittest.TestCase):

    def test1(self):
        self.assertEqual(intersectionOfNum([2, 4, 4, 2],[2, 4]), [2, 4])
    
    def test2(self):
        self.assertEqual(intersectionOfNum([1, 2, 3, 3], [3, 3]), [3])
    
    def test3(self):
        self.assertEqual(intersectionOfNum([2, 4, 6, 8], [1, 3, 5, 7]), [])

if __name__ == '__main__':
    unittest.main()

    
