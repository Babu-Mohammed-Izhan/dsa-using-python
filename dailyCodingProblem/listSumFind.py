# Given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.



import unittest

def listSumFind (array , n) :
    listNums = {}
    for i in range(len(array)):
        listNums[array[i]] = i
        diff = n - array[i]
        print(listNums)
        if diff in listNums.keys():
            return True
    return False



class TestlistSumFind(unittest.TestCase):

    def test1(self):
        self.assertEqual(listSumFind([1, 3, 8, 2],10), True)
    
    def test2(self):
        self.assertEqual(listSumFind([3, 9, 13, 7],8), False)
    
    def test3(self):
        self.assertEqual(listSumFind([4, 2, 6, 5, 2],4), True)

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately